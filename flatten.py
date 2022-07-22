input= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste=[]
def flutten(deger):
    for i in deger:
        if(type(i)==list):
            flutten(i)
        else:
            liste.append(i)

flutten(input)
print(liste)