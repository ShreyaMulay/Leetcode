# Write a program which accept range from user and display all numbers in between that range.

def RangeDisplay(start, end):
    for i in range(start,end+1):
        print(i,end=' ')

def main():
    print("Enter start : ")
    start = int(input())
    
    print("Enter end : ")
    end = int(input())

    RangeDisplay(start, end)


if __name__ == '__main__':
    main()