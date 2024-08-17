# 1. Accept number of rows and number of columns from user and display below pattern.

# Input : iRow = 4 iCol = 3
# Output : * * *
#          * * *
#          * * *
#          * * *

def Pattern(rows,cols):
    for i in range(rows):
        for j in range(cols):
            print("*",end=' ')
        print()

def main():
    print("Enter rows and cols : ")
    rows = int(input())
    cols = int(input())

    Pattern(rows,cols)


if __name__ == '__main__':
    main()