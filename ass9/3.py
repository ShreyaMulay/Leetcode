# Write a program which accept range from user and return addition of all numbers in between that range. (Range should contains positive numbers only)


def RangeSum(start, end):
    sum = 0
    if(start >=0 and end >= 0):
        for i in range(start,end+1):
            sum += i
        print(sum,end=' ')
    else:
        print("Invalid range")

    

def main():
    print("Enter start : ")
    start = int(input())
    
    print("Enter end : ")
    end = int(input())

    RangeSum(start, end)


if __name__ == '__main__':
    main()