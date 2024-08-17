# 1. Accept N numbers from user and return frequency of even numbers.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 3


def CountEven(elements):
    even = []
    
    for element in elements:
        if(element % 2 == 0):
            even.append(element)

    print("Frequency of even numbers. : ",len(even))


def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    CountEven(myList)

if __name__ == '__main__':
    main()