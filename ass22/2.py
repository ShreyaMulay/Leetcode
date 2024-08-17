# 2. Accept character from user. If character is small display its
# corresponding capital character, and if it small then display its
# corresponding capital. In other cases display as it is.

# Input : Q
# Output : q
# Input : m
# Output : M
# Input : 4
# Output : 4
# Input : %
# Output : %

def Display(char):
    data = char
    if(char.islower()):
        data = char.upper()
    elif(char.isupper()):
        data = char.lower()
    else:
        pass
    print(char , data)
def main():
    print("Enter character :")
    char = input()

    Display(char)

if __name__ == "__main__":
    main()