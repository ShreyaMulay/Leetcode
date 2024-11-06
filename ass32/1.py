# 1. Write application which accept two file names from user. Compare the contents of
# that two files. If contents are same then return true otherwise return false.
# Input : Demo.txt Hello.txt

import os
def main():
    print("Enter 1st file name ")
    f1 = input()

    print("Enter 2nd file name ")
    f2 = input()


    if(os.path.exists(f1)) and os.path.exists(f2):
        fobj1 = open(f1, 'r')

        fobj2 = open(f2, 'r')

        data1 = fobj1.read()

        data2 = fobj2.read()

        if(data1 == data2):
            print("true")
        else:
            print("false")
    else:
        print("Error while opening file ")


if __name__ == '__main__':
    main()