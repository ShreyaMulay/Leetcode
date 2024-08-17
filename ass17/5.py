# 5. Accept N numbers from user and display all such elements which are multiples of 11.
# Input : N : 6
# Elements : 85 66 3 55 93 88
# Output : 66 55 88


def Display(elements):
    divBy5 = []
    
    for element in elements:
        if(element % 11 == 0):
            divBy5.append(element)

    print("Elements which are  multiples of 11 : ",divBy5)


def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    Display(myList)

if __name__ == '__main__':
    main()