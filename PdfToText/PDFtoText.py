import pdftotext
import os
import sys


def get_done_files(output_folder):
    """
    Creates a list of files that are already done to make sure they dont have to be done twice

    :param output_folder: Folder to search through to get a list of already created files
    :return: The files that already done
    """

    # Loop through the output to find the list
    done_list = []
    for root, dirs, files in os.walk(output_folder, topdown=True):
        for file in files:

            # Get rid of the .txt extension
            done_list.append(file[:-4])

    return done_list


def get_error_files(output_folder):
    """
    Gets the error files to not have to run them again

    :param output_folder: The folder where the error file might be located
    :return: A list of errror files
    """

    error_file = output_folder + "/ErrorFiles.txt"
    errors = []
    if os.path.exists(error_file):
        with open(error_file, "r") as f:

            try:
                errors = f.readlines()
                for i in range(len(errors)):
                    errors[i] = errors[i].rstrip()
                    errors[i] = errors[i][:-4]

            except IOError:
                print("Error reading error file")

    return errors


def pdf_to_text(file_name):
    """
    Pulls text from a pdf

    :param file_name: string
    :return: the pdf as text
    """

    with open(file_name, "rb") as f:

        # Read in the pdf as text
        try:
            pdf = pdftotext.PDF(f)
            pdf = list(pdf)

            pages = ""

            # Returns output in close to original format
            if len(sys.argv) == 4 and sys.argv[3] == "f":
                for page in pdf:
                    pages += " ".join(page.split(" "))

            # Returns output in one string all separated by a space
            else:
                for page in pdf:
                    pages += " ".join(page.split())
            return pages

        except pdftotext.Error:
            return ""


def main():
    """
    Loops through a folder and creates output files for each of the files with the
    same name but with Out.txt at the end

    :return: None
    """

    # Go through each file
    folder = sys.argv[1]
    for root, dirs, files in os.walk(folder, topdown=True):
        num_files = len(files)
        i = 1

        # Create a list of the files that did not work
        errors = open(sys.argv[2] + "/ErrorFiles.txt", "a+")

        # Ensure the file is not already finished and get text if not
        done_files = get_done_files(sys.argv[2])
        error_files = get_error_files(sys.argv[2])
        done_files = done_files + error_files

        for file in files:

            if file[:-4] in done_files:
                print(str(i) + "/" + str(num_files))
                i += 1
                continue

            print(file)
            text = pdf_to_text(root + "/" + file)

            # Make sure the function returned and create a file
            if text != "":

                # Save to txt file
                out_name = sys.argv[2] + "/" + file[:-4] + ".txt"
                f = open(out_name, "w")
                f.write(text)
                f.close()

            # Add errors
            else:
                errors.write(file + "\n")

            print(str(i) + "/" + str(num_files))
            i += 1

    errors.close()
    f.close()


if __name__ == "__main__":
    main()
