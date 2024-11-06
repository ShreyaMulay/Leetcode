# 5. Write application which accept file name from user and one string from user. Write
# that string at the end of file.
# Input : Demo.txt
# Hello World
# Output : Write Hello World at the end of Demo.txt file

import os

def main():
    print("Enter the name of file  in write mode : ")
    Fname = input()
    if(os.path.exists(Fname)):
        fobj = open(Fname,"a")

        print("Enter data that u want to write in file :")
       
        data = input()
        fobj.write(data)


        fobj.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()