# 1. Write a program which displays ASCII table. Table contains symbol,Decimal, Hexadecimal and Octal representation of every member from 0 to 255.


def main():
    for value in range(128):
        print("value = {}  ASCII = {} ".format(value,chr(value)))

if __name__ == "__main__":
    main()