x=int(input("number between 1 and 100"))
import random
number=random.randint(1,100)
while x!=number:
    if x>number:
        print("high")
    elif x<number:
        print("low")
    x=int(input("number between 1 and 100"))
if x== number:
    print("correct")