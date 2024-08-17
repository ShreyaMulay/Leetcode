# Write a program which accept number from user and return the count of even digits.

def CountEven(no):
    event_count = 0
    for i in no:
        if i.isdigit():
            digit = int(i)
            if(digit % 2 == 0):
                event_count = event_count + 1
    print("event_count : ",event_count)

def CountOdd(no):
    odd_count = 0
    for i in no:
        if i.isdigit():
            digit = int(i)
            if(digit % 2 != 0):
                odd_count = odd_count + 1
    print("odd_count : ",odd_count)

def main():
    print("Enter number : ")
    no = input()

    CountEven(no)
    CountOdd(no)


if __name__ == '__main__':
    main()