# 1.Write a program which accept string from user and accept one character. Check whether that character is present in string or not.
# Input : “Marvellous Multi OS”
# e
# Output : TRUE
# Input : “Marvellous Multi OS”
# W
# Output : FALSE

def ChkChar(str1,search):
    found = False

    for i in str1:
        if(i == search):
            found = True

    if(found == True):
        print("TRUE")
    else:
        print("FALSE")

def main():
    print("Enter string :")
    str1 = input()

    print("Enter character to search in given string :")
    search = input()

    ChkChar(str1, search)

if __name__ == "__main__":
    main()