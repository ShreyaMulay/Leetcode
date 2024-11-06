# 2. Write application which accept file name and one character from user. Count the
# frequency of that character in file.
# Input : Demo.txt
# M

import os

def main():

    print("Enter file name to open :")
    fname = input()

    if(os.path.exists(fname)):
        print("Enter character to count")
        ch = input()

        fobj = open(fname, 'r')

        f1 = fobj.read()

        char_count = f1.count(ch) 

        print("Character count : " , char_count)
    else:
        print("Error while reading")


if __name__ == "__main__":
    main()