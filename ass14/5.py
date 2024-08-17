# Input : iRow = 4 iCol = 4
# Output : 1 2 3 4
#         1 * * 4
#         1 * * 4
#         1 2 3 4




def pattern(iRows, iCols):
    for i in range(iRows):
        for j in (range(iCols)):
            if(i == 0 or j == 0 or i == iRows-1 or j == iCols-1):
                print(j+1,end=' ')  
            else:
                print("*",end=' ')
            
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()