# 4. Write application which accept file name from user and display size of file.
# Input : Demo.txt
# Output : File size is 56 bytes

import os

def main():
    print("Enter the name of file   : ")
    Fname = input()
    if(os.path.exists(Fname)):
        fobj = open(Fname,"r")
        # print("File opened successfully in reading mode : ")
       
        # data = fobj.read()

        # print(data)
        fobj.seek(0,2)
        size = fobj.tell() 
        print(f"Size of file: {size} bytes")

        fobj.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()