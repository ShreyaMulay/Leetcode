# 1.Write a program which accept one number from user and print that number of even numbers on screen.


def printEven(num):
    X = 2
    for i in range(num):
       print(X)
       X = X + 2

        
def main():
    print("Enter number :")
    n = int(input())

    printEven(n)


if __name__ == '__main__':
    main()