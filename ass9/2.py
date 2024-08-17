# Write a program which accept range from user and display all even numbers in between that range.


def RangeDisplayEven(start, end):
    for i in range(start,end+1):
        if(i % 2 == 0):
            print(i,end=' ')

def main():
    print("Enter start : ")
    start = int(input())
    
    print("Enter end : ")
    end = int(input())

    RangeDisplayEven(start, end)


if __name__ == '__main__':
    main()