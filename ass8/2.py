# Write a program which accept number from user and print numbers till that number.


def Display(no):
    for i in range(1,no+1):
        print(i,end=' ')

def main():
    print("Enter number : ")
    no = int(input())

    Display(no)


if __name__ == '__main__':
    main()