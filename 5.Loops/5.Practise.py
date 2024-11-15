# print numbers from 1 to n

n = int(input("enter the number: "))
for i in range(1,n+1):
    print(i,end=" ")
print()

# print numbers from n to 1

for i in range(n,0,-1):
    print(i,end=" ")
print()

# print multiplication table of n till 10

for i in range(1,11):
    print(n," * ",i," = ",n*i)

# find the sum of n natural numbers

sum = 0
i=1
while(i<=n):
    sum += i
    i+=1
print("sum of",n,"natural numbers is: ",sum)

# find the factorial of n 

fact = 1
for i in range(1,n+1):
    fact *= i
print("factorial of",n,"natural numbers is: ",fact)