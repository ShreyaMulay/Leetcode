# 4. Accept number from user and display below pattern.
# Input : 4
# Output : # 1 * # 2 * # 3 * # 4 *


def Pattern(no):
    for i in range(1,no+1):
        print("#", i ,"*", end=' ')


def main():
    print("Enter no : ")
    no = int(input())

    Pattern(no)


if __name__ == '__main__':
    main()