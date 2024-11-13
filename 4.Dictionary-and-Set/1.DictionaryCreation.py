dict = {
    "name":"john",
    "age":25,
    "salary":250000.23,
    "skills":["java","dsa","python"]
}
print(dict["skills"])   # accessing individual element of dictionary

dict["age"] = 32  # editing the value of dictionary

print(dict)

dict["branch"] = "CSE"  # adding a new key,value to a dictionary

print(dict)  

# Nested Dictionary

dict = {
    "name" : "rahul",
    "year" : 2,
    "marks": {
        "math" : 50,
        "phy" : 45,
        "chem" : 60
    }
}

print(dict)

print(dict["marks"]["math"])  # Accessig the nestes element of the dictionary

dict = {
    "name" : "rahul",
    "name" : "rohan",      # Overwrites the previous value of the key
    "year" : 2,
    "marks": {
        "math" : 50,
        "phy" : 45,
        "chem" : 60
    }
}

print(len(dict))

