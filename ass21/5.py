# 5. Accept division of student from user and depends on the division
# display exam timing. There are 4 divisions in school as A,B,C,D. Exam
# of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM.
# (Application should be case insensitive)

# Input : C
# Output : Your exam at 9.20 AM
# Input : d
# Output : Your exam at 10.30 AM

def DisplaySchedule(div):
    if(div == 'A' or div == 'a'):
        print('Your exam at 7 AM')
    elif(div == 'B' or div == 'b'):
        print('Your exam at 8.30 AM')
    elif(div == 'C' or div == 'c'):
        print('Your exam at 9.20 AM')
    elif(div == 'D' or div == 'd'):
        print('Your exam at 10.30 AM')
    else:
        print("Invalid input")

def main():
    print("Enter division of student :")
    div = input()

    DisplaySchedule(div)


if __name__ == "__main__":
    main()