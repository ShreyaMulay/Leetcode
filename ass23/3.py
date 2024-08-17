# 3. Write a program which accept string from user and return difference between frequency of small characters and frequency of capital characters.
# Input : “MarvellouS”
# Output : 6 (8-2)

def Difference(s1):
    capital = 0
    small = 0
    diff = 0
    for i in s1:
        if(i.isupper()):
            capital = capital + 1
        elif(i.islower()):
            small = small + 1
    
    diff =  small-capital

    print(" difference between frequency of small characters and frequency of capital characters :",diff)

def main():
    print("Enter String : ")
    str1 = input()

    Difference(str1)

if __name__ == '__main__':
    main()