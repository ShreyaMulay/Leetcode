# Input : iRow = 6 iCol = 5
# Output : * * * * *
#         * @ @ @ *
#         * @ @ @ *
#         * @ @ @ *
#         * @ @ @ *
#         * * * * *




def pattern(iRows, iCols):
    for i in range(iRows):
        for j in (range(iCols)):
            if(i == 0 or j == 0 or i == iRows-1 or j == iCols-1):
                print("*",end=' ')  
            else:
                print("@",end=' ')
            
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()