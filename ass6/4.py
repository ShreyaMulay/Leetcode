# .Write a program which accept number from user and count frequency of such a digits which are less than 6.


def frequency(no):
    count = 0
    for i in str(no):
        # print(i)
        # print(i < '6')
        if(i < '6'):
            count = count + 1
   
    print("freq : ",count)


def main():
    print("Enter number :")
    n = int(input())

    frequency(n)



if __name__ == "__main__":
    main()