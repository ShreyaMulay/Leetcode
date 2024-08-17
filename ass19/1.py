# 1. Accept N numbers from user and accept one another number as NO , check whether NO is present or not.
# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : TRUE
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : FALSE




def Check(elements,search):
    flag = False    
    for element in elements:
        if(element == search):
            flag=True

    if(flag == True):
        print("TRUE")
    else:
        print("FALSE")



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