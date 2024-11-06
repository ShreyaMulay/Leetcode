# 2. Write application which accept file name from user and create that file.
# Input : Demo.txt
# Output : File created successfully.

import os

def main():
    print("Enter file name to create :")
    Fname = input()
    if(os.path.exists(Fname)):
        print("File already exists")
    else:
        open(Fname,"x")
        print("File created successfully")
    

if __name__ == "__main__":
    main()