# 4. Write a program which accept string from user and check whether it contains vowels in it or not.
# Input : “marvellous”
# Output : TRUE
# Input : “Demo”
# Output : TRUE
# Input : “xyz”
# Output : FALSE

def ChkVowel(s1):
    vowel = ['a','e','i','o','u']
    flag = False
    for i in s1:
        if i in vowel:
            flag = True

    if(flag == True):
        print("TRUE")
    else:
        print("FALSE")    

def main():
    print("Enter String : ")
    str1 = input()

    ChkVowel(str1)

if __name__ == '__main__':
    main()