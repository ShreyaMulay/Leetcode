# 3.Write a program which accept string from user and accept one character. Return index of first occurrence of that character.
# Input : “Marvellous Multi OS”
# M
# Output : 0

# Input : “Marvellous Multi OS”
# W
# Output : -1
# Input : “Marvellous Multi OS”
# e
# Output : 4

def CountChar(str1,search):
    found = False

    for i in range(len(str1)):
        ele = str1[i]
        if(ele == search):
            found = True
            print("index of first occurrence of {} character is {}".format(search,i))
            break
    
    if(found == False):
        print("Search not found ",-1)
        

   

def main():
    print("Enter string :")
    str1 = input()

    print("Enter character to search in given string :")
    search = input()

    CountChar(str1, search)

if __name__ == "__main__":
    main()