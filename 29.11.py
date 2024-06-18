car={
    "A1":"1",
    "A2":"2",
    "A3":{
         'B1':'1',
         'B2':'2',
         'B3':'3'
    }
}
cars=[]
for key,value in car.items() :
 if key=='A3':
    for B,V in car['A3']:
        cars.append(V)
for car in cars :
   print(car)
   