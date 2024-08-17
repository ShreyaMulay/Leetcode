# 4. Accept Character from user and check whether it is special symbol or not (!, @, #, $, %, ^, &, *).
# Input : %
# Output : TRUE
# Input : d
# Output : FALSE



def chkSpecial(char):
    ascii = ord(char)
    if(ascii >=33 and ascii <= 47):
        print("TRUE")
    else:
        print("FALSE")


def main():
    print("Enter character :")
    char = input()

    chkSpecial(char)

if __name__ == "__main__":
    main()