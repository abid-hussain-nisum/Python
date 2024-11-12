#check if the number entered by the user is even or odd
n = int(input("enter the number: "))

if n%2==0:
    print("even")
else:
    print("odd")

#find the greatest of 3 numbers enter the user

a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
c = int(input("enter num 3: "))

if(a>b):
    if(a>c):
        print("a is biggest")
    else:
        print("c is biggest")
else:
    if(b>c):
        print("b is biggest")
    else:
        print("c is biggest")

#check if a number is a multiple of 7 or not

num = int(input("enter the number: "))

if(num%7) == 0:
    print("multiple of 7")
else:
    print("not a multiple of 7")