# store the given data in the form of dictionary -   table:"a piece of furniture","list of facts & figures"  cat:"a small animal"

dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}

print(dict)

# you are given a list of subjects for the students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students 
# python,java,c++python,javascript,java,python,java,c++,c

list = ["python","java","c++","python","javascript","java","python","java","c++","c"]
print(len(set(list)))


# write a program to enter the marks of 3 subjects from the user and store them in a dictionary

dict = {}
dict["math"] = int(input("enter math marks: "))
dict["phy"] = int(input("enter phy marks: "))
dict["chem"] = int(input("enter chem marks: "))
print(dict)

# store 9 and 9.0 in a set as separate values in the set

set = {9,'9.0'}
# set = {("float",9.0),("int",9)}    this is another method of storing if you want to store a value and its floating value
print(set)