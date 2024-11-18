# f = open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\text.txt","r")
# data = f.read()
# print(data)
# f.close()
# print(type(data))

# Recommened to use with as it automatically closes the file. (we can avoid f.close())
# with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\text.txt", "r") as f:
#     data = f.read()
#     print(data)
# print(type(data))


# with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\text.txt","r") as f:
#     data = f.name()
#     print(data)

f = open("C://Users//mahussain//Desktop//Python//7.File-Input-and-Output//text.txt","r")
data = f.read()
print(data)