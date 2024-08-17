# 5. Accept N numbers from user and return product of all odd elements.
# Input : N : 6
# Elements : 15 66 3 70 10 88
# Output : 45

# Input : N : 6
# Elements : 44 66 72 70 10 88
# Output : 0

def Product(elements):
    eleArray = []
    prod = 1
        
    for el in elements:
        if(el % 2 !=0):
            prod = prod * el
        
    print("Product of all odd elements is ", prod)




def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)

    print("Elements are : ", myList)

    Product(myList)

if __name__ == '__main__':
    main()