# Write a program which accept number from user and display its digits in reverse order

def reversenum(num):
    rev = 0
    while(num > 0):
        ld  = num % 10
        rev = rev * 10  + ld 
        num = num // 10
    print(rev)

def main():
    print("Enter number :")
    n = int(input())
    reversenum(n)

if __name__ == "__main__":
    main()