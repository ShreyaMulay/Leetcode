# 2. Accept Character from user and check whether it is capital or not(A-Z).
# Input : F
# Output : TRUE
# Input : d
# Output : FALSE



def ChkCapital(chr):
    ascii = ord(chr)
    print("ascii",ascii)
    if(ascii >= 65 and ascii <= 90):
        print("TRUE")
    else:
        print("FALSE")
def main():
    print("Enter character :")
    chr = input()

    ChkCapital(chr)


if __name__ == "__main__":
    main()