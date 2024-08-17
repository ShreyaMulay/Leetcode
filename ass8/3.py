# 3. Write a program which accept number from user and print its numbers line.



def Display(no):
    for i in range(-no,no+1):
        print(i,end=' ')

def main():
    print("Enter number : ")
    no = int(input())

    Display(no)


if __name__ == '__main__':
    main()