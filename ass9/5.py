# Write a program which accept accept range from user and display all numbers in between that range in reverse order.

def RangeDisplayRev(start, end):
    for n in reversed(range(start,end+1)):
        print(n, end=' ')


def main():
    print("Enter start : ")
    start = int(input())
    
    print("Enter end : ")
    end = int(input())

    RangeDisplayRev(start, end)


if __name__ == '__main__':
    main()