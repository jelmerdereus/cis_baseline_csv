# importing required modules
import re
import sys
from typing import IO

# help function
def help() -> None:
    print("\nUsage:\n\tpython3 cis_to_csv.py TEXT_FILE\n")


# abort and provide help information
def aborthelp(action: str, errmsg: str) -> None:
    print(f"Error ${action}: %{errmsg}.\n")
    help()
    sys.exit(1)


# main function
if __name__ == '__main__':

    # handle input
    if len(sys.argv) != 2:
        help()
        sys.exit(1)

    # read the CIS baseline controls file extracted using pdf2txt.py
    txt_file: IO = None
    txt_content = ''

    try:
        txt_file = open(sys.argv[1], 'r', encoding='utf-8')
        txt_content = txt_file.read()
    except Exception as err:
        aborthelp('reading txt file', err.__str__())

    #make a CSV output file
    csv_file: IO = None
    try:
       csv_filename = sys.argv[1][:-4].split('/')[-1]+'.csv'
       csv_file = open(f'./{csv_filename}', 'w')
    except Exception as err:
       aborthelp('creating csv file', err.__str__())

    print('control,description,scored', file=csv_file)

    # clean text
    substitutions = [('\n', ' '), ('\t', ' '),('  ', ' ')]

    for chars, subst in substitutions:
        txt_content = txt_content.replace(chars, subst)

    # a collection of individual CIS control lines
    control_lines = [line for line in txt_content.split('..') if line != '']

    # match individual control lines with an eager pattern
    pattern = "(([0-9]{1,3}\.[0-9]{1,3}(?:\.[0-9]{1,3}|)(?:\.[0-9]{1,3}|)(?:\.[0-9]{1,3}|))\s((?:\s|)(?:(\((L1|L2)\)\s)|)(?:\s|)(Ensure)\s([\s\S]{1,200}))\((Manual|Automated|Scored|Not Scored)\))"

    for line in control_lines:
        match = re.search(pattern, line)

        if match:
            ctrl_id = match.group(2)    # 9.3.3
            ctrl_name = match.group(3)  # (L1) Ensure  'Windows Firewall ...
            ctrl_type = match.group(8)  # Scored | Not Scored | Automated | Manual

            # add a line to the CSV file
            print(f'{ctrl_id},{ctrl_name},{ctrl_type}', file=csv_file)

    # done
    csv_file.close()

    print(f'\ndone! saved results in {csv_file.name}\n')
