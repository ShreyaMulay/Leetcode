# Write a program which accept number from user and print even factors of that number.


def printEvenFactors(num):

    for i in range(1,num):
        if(num % i == 0):
            # print(i)
            if(i % 2 == 0):
                print(i, end=' ')

    # for i in range(1,num):
    #     if(i % 2 == 0 and num % i == 0):
    #         print(i)
def main():
    print("Enter number :")
    n = int(input())

    printEvenFactors(n)


if __name__ == '__main__':
    main()