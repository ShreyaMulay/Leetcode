# 4. Accept Character from user and check whether it is small case or not (a-z).
# Input : g
# Output : TRUE
# Input : D
# Output : FALSE



def ChkSmall(chr):
    ascii = ord(chr)
    print("ascii",ascii)
    if(ascii >= 97 and ascii <= 122):
        print("TRUE")
    else:
        print("FALSE")
def main():
    print("Enter character :")
    chr = input()

    ChkSmall(chr)


if __name__ == "__main__":
    main()