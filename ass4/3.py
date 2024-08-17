# 3.Write a program which accept number from user and display all its non factors.

def factors(n):
    for i in range(1,n):
        if(n%i != 0):
            print(i,end=' ')

def main():
    print("Enter number :")
    n = int(input())
    factors(n)

if __name__ == "__main__":
    main()