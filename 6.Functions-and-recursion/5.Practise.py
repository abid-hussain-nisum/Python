def sum(n):                    # recursive function to calculate the sum of n natural numbers
    if(n==1):
        return 1
    return n + sum(n-1)
print(sum(10))

def printList(list,idx):   # resursive function to print the elements of the list
    if(idx == len(list)):
        return
    print(list[idx])
    printList(list,idx+1)
list = [1,2,3,4,5,6]
printList(list,0)