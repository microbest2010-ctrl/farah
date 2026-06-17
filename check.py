esample_list=[2,3,6]
result=1
for i in esample_list:
    result*=i
    print("result=",result)

liste_type=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
liste_type.sort(key=lambda x:float(x[-1]))
print("result:",liste_type)



d1 = {'a' : 100, 'b' : 200, 'c':300}
d2 = {'a' : 300, 'b' : 200, 'd':400}

result=d1.copy()
for key,value in d2.items():
    if key in result:
        result[key]+= value
    else:
        result[key]= value  
print("result:",result)





n=8
dictionnaire={}
for i in range(1,n+1):
    dictionnaire[i]=i*i



liste_tuple=[("item1",12,20),("item2",15,10),("item3",24,5)]
liste_tuple.sort(key=lambda x: float(x[1]),reverse=True)
print("result:",liste_tuple)





exemples = {0, 1, 2, 3, 4}
print("ensemble creation:",exemples)
for element in exemples:
    print(element)

