# 5. Accept one number from user and print that number of * on screen.

# using for loop


def forAccept(num):
    print("Using for loop...")
#    print(num  *  "*")
    #    or
    for i in range(num):
        print("*",end=' ')

    print()



# using while loop

def whileAccept(num):
    print("Using while loop...")
    while(num>0):
        print("*",end=' ')
        num = num - 1
        
def main():
    print("Enter number :")
    n = int(input())

    
    forAccept(n)
    whileAccept(n)


if __name__ == '__main__':
    main()