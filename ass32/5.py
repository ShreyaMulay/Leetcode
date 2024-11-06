# 5. Accept three file names from user which are existing files. Create one new file
# named as Demo.txt. Write name and Data of that three files in Demo.txt file one
# after another.
# Input : abc.txt
# pqr.txt
# xyz.txt
# Output : Write file name and data of each file in Demo.txt file.

import os

def main():
    names = []
    for i in range(2):
        print("Enter ",i+1," file name : ")
        name = input()
        names.append(name)
    
    for n in names:
        fobj = open(n,'r')
        content = fobj.read()

        if(os.path.exists('abc.txt')):
            fp= open('abc.txt','a')
        else:
            fp= open('abc.txt','x')
        
        fp.write("\n ----------------------------------------------------------------\n")
        fp.write(n)
        fp.write("\n")
        fp.write(content)
        fp.write("\n ----------------------------------------------------------------\n")


        fobj.close()
        fp.close()


if  __name__ == "__main__":
    main()