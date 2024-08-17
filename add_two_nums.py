# 1.input given
# 9 9 9 9 9 9 9
# +
# 9 9 9 9
# ---
# 8 9 9 9 0 0 0 1
# 2.input given
# l1 = [2,4,3], l2 = [5,6,4] = [7,0,8] 


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]


class Solution:
    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2
    
    def addTwoNumbers(self):
        result = []
        carry = 0

        # Perform element-wise addition with carry-over logic
        for a, b in zip( self.list1,  self.list2):
            total = a + b + carry  # Add the carry to the current sum
        
            carry = total // 10  # Calculate the new carry (integer division by 10) // 1 is carry for 1st iterarion

            result.append(total % 10)  # Append the last digit of the total to the result //8 is reminder here 

        # Handle the final carry
        if carry > 0:
            result.append(carry)

        print("Elements wise Addition of two list is : ",result)


list1 =[]
list2 =[]

print("Enter how many numbers do u want in list1 : ")
no1 = int(input())

print("Enter elements of list1 : ")
for i in range(no1):
    l1 = int(input())
    list1.append(l1)


print("Enter how many numbers do u want in list2 : ")
no2 = int(input())

print("Enter elements of list2 : ")
for i in range(no2):
    l2 = int(input())
    list2.append(l2)

print("Original list1 is : ",list1)
print("Original list2 is : ",list2)
print()
# list1.reverse()
# list2.reverse()
# print("reverse list1 is : ",list1)
# print("reverse list2 is : ",list2)

# append the shorter list with zeros
max_len = max(len(list1), len(list2))
print(":max_len : ",max_len)
list1 = list1 + [0] * (max_len - len(list1))
print("l1 : ",list1)
list2 = list2 + [0] * (max_len - len(list2))
print("l2 : ",list2)


obj = Solution(list1,list2)
obj.addTwoNumbers()
