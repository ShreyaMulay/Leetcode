# 5. Accept N numbers from user and accept one another number as NO , return frequency of NO form it.

# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : 2
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : 0




def Frequency(elements,search):
    count = 0
    
    for element in elements:
        if(element == search):
            count = count + 1

    print("{} is present at {} times.".format(search,count))



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
   
   
    Frequency(myList,search)

if __name__ == '__main__':
    main()