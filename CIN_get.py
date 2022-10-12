///
File written by Matthew Ivler to get CINs out of annual reports using regex

ALTERNATE REGULAR EXPRESSION THAT MAY BE USED FOR A SECOND ROUND OF SCRAPING:
  reg_exp = r"[A-Za-z]{1}\d{5}[A-Za-z]{2}\d{4}[A-Za-z]{3}\d{6}"
///

import re
import glob


direct = "/data/annual_reports_tesseract/"
multi_CIN = "multiple_CINs.txt"
no_CIN = "no_CINs.txt"
outfile = "CINs.txt"
reg_exp = r"C[Ii1l]{1}N:\s{1,6}[A-Za-z]{1}\d{5}[A-Za-z]{2}\d{4}[A-Za-z]{3}\d{6}"


def get_CIN_list(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        text = infile.read()
    return re.findall(reg_exp, text)


def check_if_different(lst):
    different_CINs = []
    diff_found = False

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] != lst[j] and (lst[i] not in different_CINs):
                different_CINs.append(lst[i])
                diff_found = True
            if lst[i] != lst[j] and (lst[j] not in different_CINs):
                different_CINs.append(lst[j])
                diff_found = False
    return diff_found, different_CINs


def write_out(file_out, filename, CIN):
    with open(file_out, "a", encoding="utf-8") as outf:
        outf.write(filename + "\t" + str(CIN) + "\n")


def main():
    with open(multi_CIN, "w") as multi:
        print("multi_reset")
    with open(no_CIN, "w") as multi:
        print("none_reset")
    with open(outfile, "w") as multi:
        print("outfile reset")
    files = glob.glob(direct + "*.txt")
    for file in files:
        CIN_list = get_CIN_list(file)
        if len(CIN_list) == 0:
            write_out(no_CIN, file, "NONE")
        elif len(CIN_list) >= 1:
            different, different_lst = check_if_different(CIN_list)
            if not different:
                write_out(outfile, file, CIN_list[0])
            else:
                write_out(multi_CIN, file, different_lst)
        else:
            write_out(outfile, file, CIN_list[0])

if __name__ == "__main__":
    main()
