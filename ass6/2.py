# Write a program which accept number from user and check whether it contains 0 in it or not.

def main():
    print("Enter number :")
    n = int(input())

    if '0' in str(n):
        print("0 present")
    else:
        print("0 is not  present")

if __name__ == "__main__":
    main()