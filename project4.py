#5.1
car='audi'
a=100
b=50
c=0
t='i predicted true'
f='i predicted false'
print(car=='audi',t)
print(a>= 49 and b >= 49 ,t)
print(a>= 90 or b >= 90, t)
print(b== 0 or c == 0,t)
print(car.lower()=='audi',t)
print(c==b , f)
print(a>=101 , f)
print(a<=c , f)
print(c==0 and b==100 ,f)
print(c==a or b==c or a==b ,f)
#5.2
d='roma the best'
print('roma the best'==d , t)
print('Roma the best'==d , f)
print(d.lower=='roma the best',t)
print(d.lower=='Roma the best',f)
d=28
print(d>=10 , t)
print(d<=10 , f)
print(d>10 and d<40 , t)
print(d>=100 or d>=400 ,f)
d=['audi','volvo','bmw']
print('audi' in d , t)
print('kia' in d ,f)
#5.3
alien_color= 'red'
if alien_color=='green':
    print('+5')
else :
    print('0')
if alien_color=='red':
    print('+5')
else :
    print('0')
#5.4
if alien_color=='green':
    print('+5')
else :
    print('10')
if alien_color=='red':
    print('+5')
else :
    print('10')
#5.5
alien_color='green'
if alien_color=='green':
    print('+5')
elif alien_color=='yellow':
    print('+10')
else : print('+15')
alien_color='yellow'
if alien_color=='green':
    print('+5')
elif alien_color=='yellow':
    print('+10')
else : print('+15')
alien_color='red'
if alien_color=='green':
    print('+5')
elif alien_color=='yellow':
    print('+10')
else : print('+15')
#5.6
age=12
if age<2 :
    print("Немовля")
elif age>=2 and age<4 :
    print("Маля")
elif age>=4 and age <14 :
    print("Дитина")
elif age>=14 and age<20 :
    print("Підліток")
elif age>=20 and age<65:
    print("Дорослий")
elif age>=65:
    print("Похила людина")
else :
    print("Вік введено неправильно")
#5.7
favorite_fruits=['apple','banana','lime','mango','lemon']
t='i realy like it'
f="i don't like it "
if 'apple' in favorite_fruits :
    print(t)
else : print (f)
if 'banana' in favorite_fruits:
    print(t)
else : print (f)
if 'lime' in favorite_fruits:
    print(t)
else : print (f)
if 'pear' in favorite_fruits:
    print(t)
else : print (f)
if 'orange' in favorite_fruits:
    print(t)
else : print (f)
#5.8
a=input()
adminlist=['admin','roma','eric','taras','murad']
if a==adminlist[0]: 
    print("Hello admin, would you like to see a status report?")
elif a in adminlist :
    print("Hello ", a ," thank you for logging in again")
else : print("Sorry i don't know who you are" )
#5.9
adminlistr=[]
if adminlistr==[]:
    print("We need to find some users!")
else: print("no")
#5.10
current_users=['Roma','sacha','Misha','Ivan','Vlad']
new_users=['Roma','Vlad','Taras','tanya','olena']
for user in new_users:
    if user in current_users or user.upper() in current_users or user.title() in current_users or user.lower() in current_users :
        print("Choose another name")
    else:print("You can choose this name")
#5.11
list1_9=[1,2,3,4,5,6,7,8,9]
for list in list1_9:
    if list==1 :
        print(list,'st')
    elif list==2 :
        print(list,'nd')
    elif list==3 :
        print(list,'rd')
    else: print (list,'th')
