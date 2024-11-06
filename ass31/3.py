# 3. Write application which accept file name from user and read all data from that file
# and display contents on screen.
# Input : Demo.txt
# Output : Display all data of file.

import os

def main():
    print("Enter the name of file that you want to write  : ")
    Fname = input()
    if(os.path.exists(Fname)):
        fobj = open(Fname,"r")
        print("File opened successfully in reading mode : ")
       
        data = fobj.read()

        print(data)

        fobj.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()