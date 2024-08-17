# 1. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
# A B C D
# A B C D
# A B C D



def pattern(iRows, iCols):
    for i in range(iRows):
        for j in range(iCols):
            letter = chr(ord('A') + j)
            print(letter,end=' ')
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()