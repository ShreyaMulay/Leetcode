# Write a program which accept number from user and print that number of $ & * on screen.


def Pattern(no):
    for i in range(no):
        print("$ "," * ",end=' ')

def main():
    print("Enter number : ")
    no = int(input())

    Pattern(no)


if __name__ == '__main__':
    main()