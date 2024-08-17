# 5. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 4 iCol = 4
# Output : 1 2 3 4
#          1 * * 4
#          1 * * 4
#          1 2 3 4

def pattern(iRow, iCol):
    for i in range(iRow):
        for j in range(iCol):
            if(i == 0 or j == 0 or i == iRow-1 or j == iCol-1):
                print(j+1, end =' ')
            else:
                print("*",end =' ')
        print()

def main():
    print("Enter rows and columns : ")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()