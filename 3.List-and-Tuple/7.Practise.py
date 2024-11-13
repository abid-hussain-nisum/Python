# Ask the user to enter 3 names of movies and store it them in a list

movies = []
mov = input("enter movie 1: ")
movies.append(mov)
mov = input("enter movie 2: ")
movies.append(mov)
mov = input("enter movie 3: ")
movies.append(mov)
movies.append(input("enter movie 4: "))
print(movies)

#check if the given list is palindrome or not

list = [1,2,3,2,1]
newList = list.copy()
newList.reverse()

if(list == newList):
    print("palindrome")
else:
    print("not a palindrome")


#count the number of students with A grade in the tuple

tup = ("B","C","B","A","D","A","A")
print(tup.count("A"))

#sort the list in ascending order

list = ["B","C","B","A","D","A","A"]
list.sort()
print(list)