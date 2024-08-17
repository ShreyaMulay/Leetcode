# 5. Accept number from user and display below pattern.

# Input : 8
# Output : 2 4 6 8 10 12 14 16


def Pattern(no):
    x=2
    for i in range(no):
        print(x,end=' ')
        x=x+2

def main():
    print("Enter no : ")
    no = int(input())

    Pattern(no)


if __name__ == '__main__':
    main()