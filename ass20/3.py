# 3. Accept N numbers from user and return the difference between largest and smallest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 90 (93 -3)

def difference(list1):
    min = list1[0]
    max = list1[0]
    diff = 0

    for i in list1:
        if(i < min):
            min = i
        if(i > max):
            max = i
    diff = max - min
    print("difference between largest and smallest number is ",diff)

def main():
    print("Enter how many numbers do u want?")
    n = int(input())

    myList=[]

    print("Enter nos :")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
    
    print("List is :",myList)
    difference(myList)


if __name__ == '__main__':
    main()