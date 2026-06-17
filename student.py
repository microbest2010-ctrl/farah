student={"name":"alice","age":21,"major":"data science"}
print("student name:", student["name"])
print("keys:",list(student.keys()))
print("values:",list(student.values()))
student["age"]=22
student["graduation.year"]=2025
print("update dctionary:",student)

