# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
def palindrome(no):
    num = no
    rev = 0

    while(no > 0):
        ld = no % 10
        rev = rev * 10 + ld
        no = no // 10
    
    print("rev no is :",rev)
    if(num == rev):
        print("{} is palindrome".format(num))
    else:
        print("{} is not palindrome".format(num))



def main():
    print("Enter number : ")
    num = int(input())

    palindrome(num)

if __name__ == '__main__':
    main()