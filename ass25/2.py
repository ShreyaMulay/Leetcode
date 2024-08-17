# 2.Write a program which accept string from user and accept one character. Return frequency of that character.
# Input : “Marvellous Multi OS”
# M
# Output : 2
# Input : “Marvellous Multi OS”
# W
# Output : 0

def CountChar(str1,search):
    count = 0

    for i in str1:
        if(i == search):
            count = count + 1
    
    print("frequency of {} character is {}".format(search,count))

def main():
    print("Enter string :")
    str1 = input()

    print("Enter character to search in given string :")
    search = input()

    CountChar(str1, search)

if __name__ == "__main__":
    main()