# 2. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
# a b c d
# A B C D
# a b c d


def pattern(iRows, iCols):
    for i in range(iRows):
        for j in range(iCols):
            if(i % 2 == 0):
                letter = chr(ord('A') + j)
            else:
                letter = chr(ord('a')+ j)
            print(letter,end=' ')
        print()
        
def main():
    print("Enter rows and columns")
    rows = int(input())
    cols = int(input())

    pattern(rows, cols)


if __name__ == '__main__':
    main()