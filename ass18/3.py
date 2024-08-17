# 3. Accept N numbers from user check whether that numbers contains 11 in it or not.
# Input : N : 6
# Elements : 85 66 11 80 93 88
# Output : 11 is present
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 11 is absent



def Check(elements):
    flag = False
    
    for element in elements:
        if(element == 11):
            flag=True

    if(flag == True):
        print("11 is present")
    else:
         print("11 is absent")



def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    Check(myList)

if __name__ == '__main__':
    main()