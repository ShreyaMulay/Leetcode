# 3. Accept on number from user if number is less than 10 then print “Hello” otherwise print “Demo”

def printMsg(num):
    if(num < 10):
        print("Hello")
    else:
        print("Demo")
        
def main():
    print("Enter number :")
    n = int(input())

    printMsg(n)


if __name__ == '__main__':
    main()