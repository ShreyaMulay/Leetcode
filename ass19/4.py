# 4. Accept N numbers from user and accept Range, Display all elements from that range
# Input : N : 6
# Start: 60
# End : 90
# Elements : 85 66 3 76 93 88
# Output : 66 76 88

# Input : N : 6
# Start: 30
# End : 50
# Elements : 85 66 3 76 93 88
# Output :


def Range(elements,start,end):
    eleArray = []
        
    for index in elements:
        if(index > start and index < end):
            eleArray.append(index)
        
    print("elements from range {} {} are {}".format(start,end,eleArray))




def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)

   
    
    print("Enter the start : ")
    start = int(input())

    print("Enter the end : ")
    end = int(input())
   
    print("Elements are : ", myList)

    Range(myList,start,end)

if __name__ == '__main__':
    main()