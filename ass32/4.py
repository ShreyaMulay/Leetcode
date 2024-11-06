# 4. Write application which accept file name and one word from user. Count the
# frequency of that word in file.
# Input : Marvellous.txt
# Hello
import os
def main():
    print("Enter file name :")
    fname = input()

    if(os.path.exists(fname)):
        fobj = open(fname, 'r')

        print("Enter word to count :")
        word = input()

        f1= fobj.read()
        print('Frequency of ', word , 'is ', f1.count(word))

        fobj.close()
    else:
        print("Error while opening file :")

if __name__ == '__main__':
    main()