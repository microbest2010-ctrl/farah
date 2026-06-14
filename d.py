def echo_chamber(hello):
    return(hello+hello)
print(echo_chamber("hello"))




def greeting(a):
    return(a*2)
print(greeting(3))





def shipping(total):
    if total>=50:
        return " free shipping "
    else:
        return " shipping costs 5$ "
to1 = shipping (60) 
print(to1)  
to2 = shipping (20)
print(to2)







def upp(word):
    return word+upp() +"!!!"
print(upp("dddd"))

