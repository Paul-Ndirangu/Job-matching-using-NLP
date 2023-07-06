# ************************************************************************************************
# Code has a bug.
# Can't handle phone number extraction
# ************************************************************************************************

import re
import subprocess

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')


def extract_phone_number(file_path):
    try:
        process = subprocess.run(
            ['catdoc', '-w', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        resume_text = process.stdout.strip()
        phone_numbers = re.findall(PHONE_REG, resume_text)

        for number in phone_numbers:
            if len(number) < 16 and number in resume_text:
                return number

    except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
    
    return None


if __name__ == '__main__':
    phone_number = extract_phone_number('./files/London-Resume-Template-Professional.pdf')
    print(phone_number)
