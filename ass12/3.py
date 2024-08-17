# 3. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 3 iCol = 5
# Output : A A A A A
# B B B B B
# C C C C C


def pattern(iRows, iCols):
    for i in range(iRows):
        for j in range(iCols):
            letter = chr(ord('A') + i)
            print(letter,end=' ')
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()