#4.1
pizzas=['Маргарита','Папероні','Чотири сири']
for pizza in pizzas :
    print(pizza,", i like it.")
print('I like pizza !')
#4.2
animals=['cat','dog','chiken']
for animal in animals :
    print(animal.title()," is the best pet . ")
print('Any of these animals would make a great pet!')
#4.3 and 4.4
for value in range(1,21):
    print(value)
#4.5
list=[]
for value in range(1,101):
    list.append(value)
print(min(list))
print(max(list))
print(sum(list))
#4.6
for number in range(2,21,2):
    print(number)
#4.7
for three in range(3,31,3):
    print(three)
#4.8
for tenfirst in range (1,11):
    print(tenfirst**3)
#4.9
tenseconds=[]
for tensecond in range(1,11):
    t3=tensecond**3
    tenseconds.append(t3)
print(tenseconds)
#4.10
print(tenseconds[0:3])
print(tenseconds[4:7])
print(tenseconds[-3:])
#4.11
friend_pizzas=[]
for pizza in pizzas:
    friend_pizzas.append(pizza)
friend_pizzas.append('Австрійська')
pizzas.append('Цезар')
for pizza in pizzas :
    print('My favorite pizzas are:',pizza)
for friend_pizza in friend_pizzas :
    print("My friend’s favorite pizzas are:",friend_pizza)
#4.12
#4.13
buffets=('піца','суши','пільмені','салат','суп')
for buffet in buffets :
    print(buffet) 
buffets=('піца','суши','пільмені','борщ','капуста')
for buffet in buffets :
    print(buffet)
