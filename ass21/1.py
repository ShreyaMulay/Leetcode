# 1. Accept Character from user and check whether it is alphabet or not (A-Z a-z).
# Input : F
# Output : TRUE
# Input : &
# Output : FALSE


def ChkAlpha(chr):
    ascii = ord(chr)
    print("ascii",ascii)
    if(ascii >= 65 and ascii <= 122):
        print("TRUE")
    else:
        print("FALSE")
def main():
    print("Enter character :")
    chr = input()

    ChkAlpha(chr)


if __name__ == "__main__":
    main()