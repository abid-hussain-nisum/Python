# def sum(a,b=10):   default parameters should be declared at last 
#     return a+b
# print(sum(1))   error 

def sum(a=10,b=20):
    return a+b
print(sum(11,22))

def sum(b,a=10):
    return a+b
print(sum(10))