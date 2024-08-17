# 5. Write a program which accept N and print first 5 multiples of N.


def MultipleDisplay(no):
    for i in range(1,5+1):
        print(no*i,end=' ')

def main():
    print("Enter number : ")
    no = int(input())

    MultipleDisplay(no)


if __name__ == '__main__':
    main()