# Write a program which accept number from user and return multiplication of all digits.

def MultDigits(no):
    prod = 1
    for i in no:
        digit = int(i)
        if(digit == 0):
            digit = 1
        prod = prod * digit
    print(prod)


def main():
    print("Enter number : ")
    no = input()

    MultDigits(no)


if __name__ == '__main__':
    main()