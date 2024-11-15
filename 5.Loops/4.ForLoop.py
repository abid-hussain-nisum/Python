list = [1,2,3,4,5,6,7,8,9,0]
for i in range(1,10):
    print(i,end=" ")

tup = (1,4,9,16,25,36,49,64,81,100)
flag=False
for i in range(0,len(tup)):
    if(tup[i]==36):
        print("element found")
        flag=True
        break
if(flag==False):
    print("element not found")

seq = range(5)
print(seq[4])
print(seq)

n = 100
for i in range(1,50,2):      # range(start,end,increment)   end is always excluded
    print(i,end=" ")