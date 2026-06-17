tuple1 = (10,20,30,40)
for i in tuple1:
    print( i )  



tuple1 = (11,22)
tuple2 = (99,88)

tuple1 , tuple2 = tuple2 , tuple1
print(tuple1)
print(tuple2) 





import random
list = ("10","15","20","35","50")

random_index = random.randint(0,len(list) -1)
random_item = list[random_index]

print(random_item)



tuple1=("orange",[10,20,30],(5,15,25))
print(tuple1[1][1])

