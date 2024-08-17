# 5. Accept N numbers from user and display summation of digits of each number.
# Input : N : 6
# Elements : 8225 665 3 76 953 858
# Output : 17 17 3 13 17 21

def addition(no):
    sum = 0
    while(no > 0):
        ld = no % 10
        sum = sum +ld
        no = no //10
    return sum

def DigitsSum(list1):
    data = []
    for el in list1:
        add = addition(el)
        data.append(add)
   
    print("Summation of digits of number : ",data)

def main():
    print("Enter how many numbers do u want?")
    n = int(input())

    myList=[]

    print("Enter nos :")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
    
    print("List is :",myList)
    DigitsSum(myList)


if __name__ == '__main__':
    main()