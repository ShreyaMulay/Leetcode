# 2. Accept number from user and display below pattern.

# Input : 5
# Output : 5 # 4 # 3 # 2 # 1 #

def Pattern(no):
    for i in reversed(range(1,no+1)):
        # letter = chr(ord('A') + i)
        print(i ,"#", end=' ')


def main():
    print("Enter no : ")
    no = int(input())

    Pattern(no)


if __name__ == '__main__':
    main()