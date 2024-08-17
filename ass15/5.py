# 5. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output :    1 2 3 4
#               2 3 4
#                 3 4
#                   4



def pattern(iRows, iCols):
    for i in range(iRows):
        for j in (range(iCols+1)):
            if(i < j):
                print(j,end=' ')  
            else:
                print(" ",end=' ')
            
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()