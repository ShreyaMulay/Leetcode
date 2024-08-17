# 3. Accept Character from user and check whether it is digit or not (0-9).
# Input : 7
# Output : TRUE
# Input : d
# Output : FALSE



def ChkDigit(chr):
    ascii = ord(chr)
    print("ascii",ascii)
    if(ascii >= 48 and ascii <= 57):
        print("TRUE")
    else:
        print("FALSE")
def main():
    print("Enter character :")
    chr = input()

    ChkDigit(chr)


if __name__ == "__main__":
    main()