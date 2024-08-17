# Write a program which accept range from user and return addition of all even numbers in between that range. (Range should contains positive numbers only)


def RangeSumEven(start, end):
    sum = 0
    if(start >=0 and end >= 0):
        for i in range(start,end+1):
            if(i%2 == 0):
                sum += i
        print(sum,end=' ')
    else:
        print("Invalid range")

    

def main():
    print("Enter start : ")
    start = int(input())
    
    print("Enter end : ")
    end = int(input())

    RangeSumEven(start, end)


if __name__ == '__main__':
    main()