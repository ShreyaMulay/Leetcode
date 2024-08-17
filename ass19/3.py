# 3. Accept N numbers from user and accept one another number as NO , return index of last occurrence of that NO.
# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : 3
# Input : N : 6
# NO: 93
# Elements : 85 66 3 66 93 88
# Output : 4
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : -1


def Check(elements,search):
    eleIndex = -1
        
    for index in range(len(elements)):
        ele = elements[index]
        if(ele == search):
            eleIndex = index
            
    
    print("Index of {} is {}".format(search,eleIndex))




def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)

    print("Elements are : ", myList)
    
    print("Enter the number to search : ")
    search = int(input())
   
   
    Check(myList,search)

if __name__ == '__main__':
    main()