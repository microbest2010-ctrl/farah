with open("notes.txt","w")as file :
    file.write("name:farah")
    file.write("age:16")


with open("notes.txt","r")as file : 
    print(file.read())   


with open("notes.txt","a")as file :
    file.write("hobby:sport")

with open("notes.txt","r")as file :
    print(file.read())

