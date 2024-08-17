# 5. Accept number from user and check whether number is even or odd.

def EvenOdd(n1):
    if(n1 % 2 == 0):
        print("Even number")
    else:
        print("Odd number")
    

def main():
    print("Enter  number :")
    n1 = int(input())

    EvenOdd(n1)


if __name__ == '__main__':
    main()