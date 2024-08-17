# 4. Accept N numbers from user and return frequency of 11 form it.
# Input : N : 6
# Elements : 85 66 3 15 93 88
# Output : 0
# Input : N : 6
# Elements : 85 11 3 15 11 111
# Output : 2



def Frequency(elements):
    count = 0
    
    for element in elements:
        if(element == 11):
            count = count + 1

    print("11 is present at {} times.".format(count))



def main():
    print("How many numbers do u want ? ")
    n = int(input())

    myList = []
    print("Enter the numbers : ")
    for i in range(n):
        nos = int(input())
        myList.append(nos)
   
    print("Elements are : ", myList)
    Frequency(myList)

if __name__ == '__main__':
    main()