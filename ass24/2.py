# 2.Write a program which accept string from user and convert it into
# upper case.
# Input : “Marvellous Multi OS”
# Output : MARVELLOUS MULTI OS

def struprx(s1):
    str1 = ''
    for i in s1:
        if(i.islower()):
            str1 = str1 + i.upper()
        else:
            str1 = str1 + i

    print("Upper case string is : ",str1)

def main():
    print("Enter String :")
    str1 = input()

    struprx(str1)


if __name__ == '__main__':
    main()