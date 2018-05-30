import os
from shutil import copyfile


def main():
    print('Welcome to Flask generator')
    curr = os.getcwd()
    print(curr)
    print("Help: ")
    directory = input("Directory for the project: ")
    if os.path.exists(directory):
        print("The directory already exists")
        exit(0)
    else:
        entry_file = input("Name of entry file (.py): ")
        if not entry_file.endswith(".py"):
            entry_file = entry_file + ".py"

        # create the project directory
        os.mkdir(directory)
        # copy the main.txt file to the directory
        copyfile(curr + '/main.txt', directory + "/main.txt")
        # rename the file name also change the extension to .py
        os.renames(directory + '/main.txt', directory + "/" + entry_file)
        print("File created")
        exit(0)


main()
