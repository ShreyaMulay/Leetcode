# Write a program which accept number from user and return difference between summation of all its factors and non factors.

def factors(n):
    sum1 =0
    sum2 =0
    sum = 0

    for i in range(1,n):
        if(n%i == 0):
            sum1 = sum1 + i
        else:
            sum2 = sum2 + i
    sum = sum1 - sum2
    print(sum)

def main():
    print("Enter number :")
    n = int(input())
    factors(n)

if __name__ == "__main__":
    main()