# 1.Write a program which accept string from user and count number of capital characters.
# Input : “Marvellous Multi OS”
# Output : 4


def CountCapital(s1):
    count = 0
    for i in s1:
        if(i.isupper()):
            count = count + 1
    print("Number of capital characters :",count)

def main():
    print("Enter String : ")
    str1 = input()

    CountCapital(str1)

if __name__ == '__main__':
    main()