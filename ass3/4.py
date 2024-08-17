# 5. Accept on character from user and check whether that character is vowel (a,e,i,o,u) or not.

def main():
    vowel = ['a', 'e', 'i', 'o', 'u']

    print("Enter character :")
    chr = input()

    if chr in vowel:
        print("character is vowel")
    else:
        print("character is not vowel")

if __name__ == "__main__":
    main()