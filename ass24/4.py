# 4. Write a program which accept string from user and display only digits from that string.
# Input : “marve89llous121”
# Output : 89121
# Input : “Demo”
# Output :

def DisplayDigit(s1):
    str1 = ''
    for i in s1:
        if(i.isdigit()):
            str1 = str1 + i

    print("digits from string is : ",str1)

def main():
    print("Enter String :")
    str1 = input()

    DisplayDigit(str1)


if __name__ == '__main__':
    main()