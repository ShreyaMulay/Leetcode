# input : 987  output : 24 sum = 6
print("Enter no:")
no = int(input())

while(no > 9):
    sum = 0

    while(no > 0):
        ld = no % 10
        sum = sum + ld
        no = no // 10
    
    no = sum

print(sum)


