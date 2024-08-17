# 3.Write a program which accept number from user and return the count of digits in between 3 and 7.

def CountRange(no):
    count = 0
    for i in no:
        digit = int(i)
        if(digit >3 and digit<7):
            count += 1
    print(count)


def main():
    print("Enter number : ")
    no = input()

    CountRange(no)


if __name__ == '__main__':
    main()