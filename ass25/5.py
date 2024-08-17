# 5. Write a program which accept string from user reverse that string in place.
# Input : “abcd”
# Output : “dcba”
# Input : “abba”
# Output : “abba”

def StrRevX(str1):
    string = ''

    for i in reversed(str1):
        string = string + i 
  
    print("reverse of {} string is {} ".format(str1, string))
        

   

def main():
    print("Enter string :")
    str1 = input()
   
    StrRevX(str1)

if __name__ == "__main__":
    main()