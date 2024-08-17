# Write a program which accept number from user and display its multiplication of factors.

def factors(n):
    prod =1
    for i in range(1,n):
        if(n%i == 0):
            prod = prod * i
            print(prod)

def main():
    print("Enter number :")
    n = int(input())
    factors(n)

if __name__ == "__main__":
    main()