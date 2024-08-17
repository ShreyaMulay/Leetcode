# 2. Write a program which accept string from user and count number of small characters.
# Input : “Marvellous”
# Output : 9

def CountSmall(s1):
    count = 0
    for i in s1:
        if(i.islower()):
            count = count + 1
    print("Number of small characters :",count)

def main():
    print("Enter String : ")
    str1 = input()

    CountSmall(str1)

if __name__ == '__main__':
    main()