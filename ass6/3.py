# 3.Write a program which accept number from user and count frequency of 2 in it.

def frequencyOf2(n):
    count = 0
    for i in n:
        if i == '2':
            count = count + 1
       
    print("frequency of  2 is : ",count)
    print()

def frequencyOf4(n):
    count = 0
    for i in n:
        if i == '4':
            count = count + 1
       
    print("frequency of  4 is : ",count)


def main():
    print("Enter number :")
    n = input()

    frequencyOf2(n)
    frequencyOf4(n)



if __name__ == "__main__":
    main()