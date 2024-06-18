#7.1
car=input('What car you want : ')
print('Let me see if I can find you a ',car)
#7.2
people=input('How many prople will be in your paty ? \n Please enter : ')
people=int(people)
if people>8 :
    print("Please wait")
elif people<=8 :
    print('We can offer 4 table')
else : print('Sorry')
#7.3
number=input('Enter number : ')
number=int(number)
if number%10==0 :
    print("Число кратне 10 ")
else : print("Число не кратне 10")
#7.4
a=True
while a :
    b=input("Добавте інгридієнти до піци , якщо не птрібно напишіть quit : ")
    if b != 'quit':
        print("інгридієнт добавлено ")
    else : a=False
#7.5 
b=True
while b:
    a=input("Білети в кіно. Введіть ваш вік : ")
    a=int(a)
    if a<3 :
        print('Білет безкоштовний  ')
        break
    elif a>=3 and a<=12 :
        print('білет коштує 10$ ')
        break
    else:
        print('білет коштує 15$ ') 
        break
#7.6(7.4)
a=0
active=input("Як довго продовжувати цикл : ")
active=int(active)
while a<active :
    b=input("Добавте інгридієнти до піци , якщо не птрібно напишіть quit : ")
    if b != 'quit':
        print("інгридієнт добавлено ")
    else : break
    a+=1
#7.7
#a=True
#while a:
#    print ('Hello')
#7.8
sandwich_oders=["pastrami","pastrami","fish","meat","vegeterien","pastrami"]
finished_sandwiches=[]
while "pastrami" in sandwich_oders:
    sandwich_oders.remove("pastrami")
while sandwich_oders:
    finished_sandwich=sandwich_oders.pop()
    finished_sandwiches.append(finished_sandwich)
    print(finished_sandwich , " is done")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
#7.10
a=True
holidays={}
while a:
    name=input("what your name (no) : ")
    if name=="no":
        break
    else:
        holiday=input("where you would go on holiday : ")
        holidays[name]=holiday
print(holidays)