# 5. Accept character from user and display its ASCII value in decimal,
# octal and hexadecimal format.
# Input : A
# Output : Decimal 65
# Octal 0101
# Hexadecimal 0X41


def Display(char):
  print("Input : " , char)
  ascii = ord(char)
  print("Decimal : " , ascii)
  print("Octal : " , oct(ascii))
  print("Hexadecimal : " , hex(ascii))

def main():
    print("Enter character :")
    char = input()

    Display(char)

if __name__ == "__main__":
    main()