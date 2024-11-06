# 3. Write application which accept two file names from user. Append the contents of
# first file at the end of second file.
# Input : Demo.txt Hello.txt
# Output : Concat contents of Demo.txt at the end of Hello.txt


import os

def main():
    print("Enter the 1st  name of file  in write mode : ")
    Fname1 = input()

    print("Enter the 2nd name of file  in write mode : ")
    Fname2 = input()


    if(os.path.exists(Fname1) and os.path.exists(Fname2)) :
        fobj1 = open(Fname1,"a")

        fobj2 = open(Fname2,"r")

        ff = fobj2.read()
        fobj1.write(ff)


        fobj1.close()
        fobj2.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()