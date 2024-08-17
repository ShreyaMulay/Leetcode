# 1. Accept number from user and display below pattern.

# Input : 5
# Output : A B C D E
def Pattern(no):
    for i in range(no):
        letter = chr(ord('A') + i)
        print(letter, end=' ')


def main():
    print("Enter no : ")
    no = int(input())

    Pattern(no)


if __name__ == '__main__':
    main()