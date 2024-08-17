# 4. Accept two numbers from user and display first number in second number of times.


def printNo(n1, n2):
    for i in range(n2):
        print(n1,end=' ')

def main():
    print("Enter 1st number :")
    n1 = int(input())

    print("Enter 2nd number :")
    n2 = int(input())

    printNo(n1,n2)


if __name__ == '__main__':
    main()