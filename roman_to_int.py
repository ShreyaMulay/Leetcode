# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
def romanToIntConverter(rNo):

    dictionary = {
        'I':1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000 
    }

    integer_value = 0
    prev_value = 0
   
    for char in reversed(rNo):
        value = dictionary[char]
        print("char and value = {} {}".format(char, value))
        print("value < prev_value : ",value < prev_value)
        if value < prev_value:
            integer_value = integer_value - value
        else:
            integer_value = integer_value + value
        print("::integer_value",integer_value)
        prev_value = value

    print("Integer value is {} for {} roman char  ".format(integer_value,rNo))



def main():
    print("Enter roman number :")
    romanNo = input()

    romanToIntConverter(romanNo)

if __name__ == "__main__":
    main()