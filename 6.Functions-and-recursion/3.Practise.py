def lengthOfList(list):                       # function to print the lenght of the list and print the list elements in a single line
    print("the size of list is: ",len(list))
    for i in list:
        print(i,end=" ")
    print()

def factorialOfN(n):            # function to print the factorial of n
    fact=1
    for i in range(1,n+1):
        fact *= i
    print("factorial of",n,"is:",fact)

def USD_to_INR(dollar):        # function to convert usd to inr
    print(dollar,"dollars in rupees is:",dollar*82.2)


list = [1,2,3,4,5,6,7]
lengthOfList(list)
factorialOfN(10)
USD_to_INR(5)

