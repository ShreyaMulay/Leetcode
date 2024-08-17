# 5. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 3 iCol = 4
# Output : 1 2 3 4
# 5 6 7 8
# 9 10 11 12



def pattern(iRows, iCols):
    num = 1
    for i in range(iRows):
        for j in range(iCols):
            print(num,end=' ')
            num = num + 1
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()