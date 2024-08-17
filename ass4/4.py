# 4.Write a program which accept number from user and return summation of all its non factors.

def factors(n):
    sum =0
    for i in range(1,n):
        if(n%i != 0):
            sum = sum + i
    print(sum)

def main():
    print("Enter number :")
    n = int(input())
    factors(n)

if __name__ == "__main__":
    main()