dict = {
    "name" : "rahul",
    "year" : 2,
    "marks": {
        "math" : 50,
        "phy" : 45,
        "chem" : 60
    }
}
new = {
    "sub" : 55
}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
print(dict.update(new))

list = list(dict.items())
print(list)