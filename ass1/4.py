# 4. Accept one number and check whether is is divisible by 5 or not.

def checkDiv(num):
    if(num % 5 == 0):
        print("divisible by 5")
    else:
        print("not divisible by 5")
        
def main():
    print("Enter number :")
    n = int(input())

    checkDiv(n)


if __name__ == '__main__':
    main()