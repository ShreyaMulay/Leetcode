# 2. Accept N numbers from user and return difference between frequency of even number and odd numbers.
# Input : N : 7
# Elements : 85 66 3 80 93 88 90
# Output : 1 (4 -3)



def Frequency(elements):
    even = []
    odd = []
    sum = 0
    
    for element in elements:
        if(element % 2 == 0):
            even.append(element)
        else:
            odd.append(element)

    sum = len(even) - len(odd)
    print("Difference between frequency of even number and odd numbers. : ",sum)


def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    Frequency(myList)

if __name__ == '__main__':
    main()