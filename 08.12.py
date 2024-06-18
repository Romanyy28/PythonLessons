def numbers(listnumber,dellistnumber):
    list=[]
    a=0
    while a<listnumber:
        list.append(listnumber)
        listnumber=listnumber-1
    while a<dellistnumber:
        list.pop(dellistnumber-1)
        dellistnumber=dellistnumber-1
    return list
b=numbers(10,3)
print(b)



