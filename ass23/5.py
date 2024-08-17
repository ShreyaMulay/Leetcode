# 3. Write a program which accept string from user and display it inn reverse order.
# Input : “MarvellouS”
# Output : “SuollevraM”

def Reverse(s1):
    rev = ''
    for i in reversed(s1):
        rev = rev + i

    print("rev string is : ",rev)
def main():
    print("Enter String : ")
    str1 = input()

    Reverse(str1)

if __name__ == '__main__':
    main()