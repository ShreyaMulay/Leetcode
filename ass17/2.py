# 2. Accept N numbers from user and display all such elements which are divisible by 5.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 85 80



def Display(elements):
    divBy5 = []
    
    for element in elements:
        if(element % 5 == 0):
            divBy5.append(element)

    print("Elements which are divisible by 5 : ",divBy5)


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