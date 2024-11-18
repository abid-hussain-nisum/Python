# create a file and insert the data
with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\Practise.txt","w+") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    data = f.read()
    print(data)
    
#overwrite the existing file
with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\Practise.txt","r") as f:
    data = f.read()
    str =  data.replace("Java","Python")
with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\Practise.txt","w+") as f:
    f.write(str)

#check if learning exists in the file or not
with open("C:\\Users\\mahussain\\Desktop\\Python\\7.File-Input-and-Output\\Practise.txt","r") as f:
    data = f.read()
    if(data.find("learning")!=-1):
        print("exists")
    else:
        print("does not exists")

