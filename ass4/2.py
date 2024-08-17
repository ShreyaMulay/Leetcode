# Write a program which accept number from user and display its factors in decreasing order.

def factors(n):
    fact = []
    for i in range(1,n):
        if(n%i == 0):
            fact.append(i)
    fact.reverse()
    print(fact)

def main():
    print("Enter number :")
    n = int(input())
    factors(n)

if __name__ == "__main__":
    main()