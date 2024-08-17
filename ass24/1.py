# 1.Write a program which accept string from user and convert it into
# lower case.
# Input : “Marvellous Multi OS”
# Output : marvellous multi os


def strlwrx(s1):
    str1 = ''
    for i in s1:
        if(i.isupper()):
            str1 = str1 + i.lower()
        else:
            str1 = str1 + i

    print("Lower case string is : ",str1)

def main():
    print("Enter String :")
    str1 = input()

    strlwrx(str1)


if __name__ == '__main__':
    main()