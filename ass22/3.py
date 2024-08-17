# 3. Accept character from user. If it is capital then display all the
# characters from the input characters till Z. If input character is small
# then print all the characters in reverse order till a. In other cases
# return directly.
# Input : Q
# Output : Q R S T U V W X Y Z
# Input : m
# Output : m l k j i h g f e d c b a
# Input : 8
# Output :

def Display(char):
    if(char.isupper()):
        ascii = ord(char)
        for i in range(ascii,91):
            print(chr(i),end = " ")
    elif(char.islower()):
        no = ord(char)
        # print("no",no)
        for i in reversed(range(97,no+1)):
            print(chr(i),end = " ")
    else:
        print(char)


def main():
    print("Enter character :")
    char = input()

    Display(char)

if __name__ == "__main__":
    main()