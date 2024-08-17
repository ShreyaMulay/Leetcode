# Write a program which accept number from user and return difference between summation of even digits and summation of odd digits.

def CountDiff(no):
    sum=0
    evenSum=0
    oddSum=0

    for i in no:
        digit = int(i)
        if(digit % 2 == 0):
            evenSum += digit
        else:
            oddSum += digit
    sum = evenSum - oddSum
    print(sum)

def main():
    print("Enter number : ")
    no = input()

    CountDiff(no)


if __name__ == '__main__':
    main()