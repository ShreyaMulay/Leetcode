# 4. Accept one character from user and convert case of that character.

def main():
    print("Enter character :")
    chr = input()
    
    print("character is : ",chr )
    if(chr.islower()):
        chr = chr.upper()
    else:
        chr = chr.lower()

    print("character after converting : ",chr )


if __name__ == "__main__":
    main()