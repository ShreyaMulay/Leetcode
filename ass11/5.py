# 5. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 4 iCol = 4
# Output : 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4


def pattern(iRows, iCols):
    for i in range(1,iRows+1):
        for j in range(iCols):
            print(i,end=' ')
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()