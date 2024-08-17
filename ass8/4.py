# 4. Write a program which accepts N from user and print all odd numbers up to N.


def OddDisplay(no):
    for i in range(no):
        if(i%2 != 0):
            print(i,end=" ")
def main():
    print("Enter number : ")
    no = int(input())

    OddDisplay(no)


if __name__ == '__main__':
    main()