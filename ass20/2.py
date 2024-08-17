# 2. Accept N numbers from user and return the smallest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 3

def smallest(list1):
    min = list1[0]
    print(max)

    for i in list1:
        if(i < min):
            min = i
    print("smallest number is ",min)

def main():
    print("Enter how many numbers do u want?")
    n = int(input())

    myList=[]

    print("Enter nos :")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
    
    print("List is :",myList)
    smallest(myList)


if __name__ == '__main__':
    main()