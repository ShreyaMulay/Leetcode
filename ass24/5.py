# 5. Write a program which accept string from user and count number of white spaces
# Input : “MarvellouS”
# Output : 0
# Input : “MarvellouS Infosystems”
# Output : 1
# Input : “MarvellouS Infosystems by Piyush Manohar Khairnnar”
# Output : 5

def CountWhite(s1):
    count = 0
    for i in s1:
        if(i == ' '):
            count = count + 1

    print("number of white spaces : ",count)

def main():
    print("Enter String :")
    str1 = input()

    CountWhite(str1)


if __name__ == '__main__':
    main()