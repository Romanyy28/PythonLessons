#6.1
Man={'first_name':'Roma','last_name':'trotsiuk','age':'18','city':'Lutsk'}
print(Man['first_name'],Man['last_name'],Man['age'],Man['city'])
#6.2
numbers={'Roma':'8','Olena':'28','Ivan':'56','Taras':'78','Vlad':'18'}
print(numbers['Ivan'],numbers['Olena'],numbers['Roma'],numbers['Taras'],numbers['Vlad'])
#6.3
terms={
    "Алгоритм":" чітко задана послідовність кроків, які мають бути виконані для розв’язання завдання.",
    "Тренаж":"Тренування, а також комплекс вправ для тренування в чому-небудь",
    "Інформатика":"це наука, яка вивчає закони i методи накопичення, опрацювання i передачi iнформацiї в природних, технiчних i соцiальних системах з використанням комп’ютерної техніки.",
    "Iнформацiя":"це данi про явища, процеси та предмети навколишнього середовища.",
    "Повідомлення":"це різні форми подання якої-небудь інформації.",
    "Програма":"план дiй, який пiдлягає виконанню певним виконавцем.",
    "Програмування":"це розробка програм для різних обчислювальних і керуючих пристроїв.",
    "Програміст":"це висококваліфікований спеціаліст, який створює комп’ютерні програми.",
    "Моделювання":"це процес створення і дослідження моделі."
}
print("Алгоритм","-",terms['Алгоритм'],"\n","Тренаж","-",terms['Тренаж'],"\n","Інформатика","-",terms["Інформатика"],"\n","Iнформацiя","-",terms["Iнформацiя"],"\n","Повідомлення","-",terms["Повідомлення"],"\n","Програма","-",terms["Програма"])
#6.4
for key,value in terms.items():
    print(key)
    print(value)
#6.5
rivers={
    "Сена":"Франція",
    "Ізер":"Бельгія",
    "Дніпро":"Україна"
}
for key,value in rivers.items():
    print(key , " річка яка протікає в ", value)
for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)
#6.6
favorite_languages = {
'jen': 'python',
'sarah': 'c++',
'edward': 'ruby',
'phil': 'python',
}
peoples=["Roma","Vlad","Dima",'phil','edward','sarah','jen']
for people in peoples:
    if people in favorite_languages.keys():
        print("You done test")
    elif people not in favorite_languages.keys():
        print("Please do test")
    else: print("Who are you ?")
#6.7
people={
    "man1":{'first_name':'Roma','last_name':'trotsiuk','age':'18','city':'Lutsk'},
    "man2":{'first_name':'Vlad','last_name':'trotsiuk','age':'22','city':'Lutsk'},
    "man3":{'first_name':'Oleg','last_name':'trotsiuk','age':'38','city':'Lutsk'}
}
for mans,mansinfo in people.items():
    print("\n first_name:",mansinfo['first_name'],'\n last_name :',mansinfo['last_name'],'\n age :', mansinfo['age'],"\n city :",mansinfo['city'])
#6.8
pets={
    "Busa":{"pet":"cat","people":"Roma"},
    "Tom":{"pet":"cat","people":"Sacha"}
    }
print(pets)
#6.9
favorite_places={
    "Universety":["roma","arsen","vlad"],
    "McDonalds":["vlad","arsen","Olena"],
    "MoJo":["olena","roma",'vlad']
}
print(favorite_places)
#6.10
numbers={
    'Roma':[8,11],
    'Olena':[28,23],
    'Ivan':[56,5],
    'Taras':[78,8],
    'Vlad':[18,90]
    }
for key , value in numbers.items():
    print(key,"s favorit numbers is :",value)
#6.11
cities={
    'Lutsk':{'country':'Ukraine','people':'200 000','fact':'a city of regional significance in the west of Ukraine'},
    'Kyiv':{'country':'Ukraine','people':'4 000 000','fact':'the capital and largest city of Ukraine'},
    'New York':{'country':'USA','people':'8 000 000','fact':'the largest city in the USA'}
}
for key , value in cities.items():
    print(key,"\n country :",value['country'],"\n people :",value['people'],"\n fact :",value['fact'])