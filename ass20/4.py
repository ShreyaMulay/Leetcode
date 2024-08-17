# 4. Accept N numbers from user and display all such numbers which contains 3 digits in it.
# Input : N : 6
# Elements : 8225 665 3 76 953 858
# Output : 665 953 858

def Digits(list1):
    data = []
    for el in list1:
        # print("el",el)
        el = str(el)
        # print("el",len(el))
        if(len(el) == 3):
            el = int(el)
            data.append(el)

   
    print("numbers which contains 3 digits in it are : ",data)

def main():
    print("Enter how many numbers do u want?")
    n = int(input())

    myList=[]

    print("Enter nos :")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
    
    print("List is :",myList)
    Digits(myList)


if __name__ == '__main__':
    main()