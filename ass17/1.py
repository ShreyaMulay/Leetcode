# 1. Accept N numbers from user and return difference between summation of even elements and summation of odd elements.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 53 (234 - 181)

def Difference(elements):
    evenArray = []
    oddArray = []
    evenSum = 0
    oddSum = 0
    sum = 0


    for element in elements:
        if(element % 2 == 0):
            evenArray.append(element)
        else:
            oddArray.append(element)
    # print(evenArray)
    # print(oddArray)

    for even in evenArray:
        evenSum = evenSum + even

    for odd in oddArray:
        oddSum = oddSum + odd

    # print(evenSum)
    # print(oddSum)

    sum = evenSum - oddSum
    print("difference between summation of even elements and summation of odd elements : ",sum)


def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    Difference(myList)

if __name__ == '__main__':
    main()