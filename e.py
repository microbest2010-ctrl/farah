def calcul(num1,num2):
    a=input("enterthe operator (+,*,-,/)")
    if a =="+":
        return(num1 + num2) 
    elif a =="*":
        return(num1 * num2)
    elif a =="-":
        return(num1 - num2)
    elif a =="/":
        return(num1 / num2)
print(calcul(5,6))
  