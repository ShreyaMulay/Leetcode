# input : 987  output : 24 sum = 6
print("Enter 3 no:")
a = int(input())
b = int(input())
c = int(input())

if(a>b and a>c):
    max = a
elif(b>a and b>c):
    max = b
else:
    max = c

print("Max :",max)


