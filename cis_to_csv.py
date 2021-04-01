# importing required modules
import re
import sys
import PyPDF2

# help function
def help() -> None:
    print("\nUsage:\n\tpython3 cis_to_csv.py <PATH>\n")


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

    # read the PDF file
    try:
        pdf_file = open(sys.argv[1], 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    except Exception as err:
        aborthelp('reading pdf file', err.__str__())

    # make an output file
    try:
        csv_filename = sys.argv[1][:-4].split('/')[-1]+'.csv'
        csv_file = open(f'./{csv_filename}', 'w')
    except Exception as err:
        aborthelp('creating csv file', err.__str__())

    print('control,description,scored', file=csv_file)

    toc_start = False
    toc_end = False

    # loop over Table of Content Pages
    for page_id in range(pdf_reader.numPages):
        page_object = pdf_reader.getPage(page_id)
        page_text = page_object.extractText()

        # clean text
        clean_text = page_text.replace('\n', '')

        # debug
        print(f'\nCLEAN TEXT ON PAGE {page_id}:\n\n== START ==\n{clean_text}\n== END ==\n\n')

        if toc_end:
            break
        elif not toc_start:
            if 'Table of Contents' not in page_text:
                continue
            else:
                # first page of Table of Contents
                toc_start = True
        elif 'Appendix: ' in page_text:
            # last page of Table of Contents
            toc_end = True
        

        # use a regular expression to find CIS baseline controls
        pattern = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(?:\.[0-9]{1,3}|)(?:\.[0-9]{1,3}|)\s[^.]{10,300}\s\((?:Not\s|)Scored\)'
        page_results = re.findall(pattern, clean_text)

        # extract 3 pieces of information
        for ctrl_string in page_results:
            words = ctrl_string.split(' ')

            control_id = words[0]
            description = ' '.join(words[1:]).replace('(Scored)', '').replace('(Not Scored)', '')

            if words[-1] == '(Scored)':
                scored = 'Yes'
            else:
                scored = 'No'

            print(f'{control_id},{description},{scored}', file=csv_file)

    # all pages have been scanned
    csv_file.close()

    print(f'\ndone! saved results in {csv_file.name}\n')
