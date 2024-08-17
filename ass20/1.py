# 1. Accept N numbers from user and return the largest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 93

def largest(list1):
    max = list1[0]
    print(max)

    for i in list1:
        if(i > max):
            max = i
    print("largest number is ",max)

def main():
    print("Enter how many numbers do u want?")
    n = int(input())

    myList=[]

    print("Enter nos :")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
    
    print("List is :",myList)
    largest(myList)


if __name__ == '__main__':
    main()