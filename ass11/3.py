# 3. Accept number of rows and number of columns from user and display below pattern.
# Input : iRow = 3 iCol = 5
# Output : 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1


def Pattern(rows,cols):
    for i in range(rows):
        for j in reversed(range(1,cols+1)):
            print(j,end=' ')
        print()

def main():
    print("Enter rows and cols : ")
    rows = int(input())
    cols = int(input())

    Pattern(rows,cols)


if __name__ == '__main__':
    main()