# 3.Write a program which accept string from user and toggle the case.
# Input : “Marvellous Multi OS”
# Output : mARVELLOUS mULTI os

def strtogglex(s1):
    str1 = ''
    for i in s1:
        if(i.islower()):
            str1 = str1 + i.upper()
        else:
            str1 = str1 + i.lower()

    print("Upper case string is : ",str1)

def main():
    print("Enter String :")
    str1 = input()

    strtogglex(str1)


if __name__ == '__main__':
    main()