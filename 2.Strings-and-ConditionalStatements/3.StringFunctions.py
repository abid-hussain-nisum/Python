str = "how hello! how are you doing?"

print(str.endswith("ing?"))  #returns true if the string ends with substr
print(str.capitalize()) #capitalizes the first character
print(str.replace("how","HOW")) #replaces the old occurence with new
print(str) #original string is not changed
print(str.find("a"))  #returns the 1st index of the 1st occurrer
a = str.count("how")  #counts the occurence of substr in string
print(a)
