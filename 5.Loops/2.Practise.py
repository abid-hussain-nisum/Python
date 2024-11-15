# print 1 to n 

# n = int(input("enter the number: "))
# i=1
# while(i<=n):
#     print(i,end=" ")
#     i+=1

# print n to 1

# n = int(input("enter the number: "))
# i=n
# while(i>=1):
#     print(i,end=" ")
#     i-=1

# print multiplication table of n

# n = int(input("enter the number: "))
# i=1
# while(i<=10):
#     print(n,"*",i,"=",n*i)
#     i+=1

# print the squares till n 

# n = int(input("enter the number: "))
# i=1
# while(i<=n):
#     print(i**2,end=" ")
#     i+=1

# find the number x in the tuple

tup = (1,2,3,4,5,6,7,8,9)
flag = False
target = 4
i = 0
while(i<len(tup)):
    if(tup[i]==target):
        print("element found at index",i+1)
        flag=True
        break
    i+=1
if(flag == False):
    print("element not found in the tuple")