#8.1
def display_message():
    print("Эта глава посвящена функциям — именованным блокам кода, предназначенным для решения одной конкретной задачи.")
display_message()
#8.2
def  favorite_book(book):
    print("My favorit book is ", book)
favorite_book("Manga")
def make_shirt(size="L",printX="I love Python "):
    print("We will make t-shirt wich size is ",size," and with print ",printX)
make_shirt('S',"The best")
#8.4
make_shirt()
make_shirt("S","Good boy")
#8.5
def describe_city(city,country='Ukraine'):
    print(city,"is in ",country)
describe_city('lviv')
describe_city('lutsk')
describe_city('london','united kingdom of grait britan')
#8.6
def city_country(city,country):
    city_country=city+","+country
    return city_country
print(city_country('rome','italy'))
print(city_country('lviv','ukraine'))
print(city_country('berlin','deutchland'))
#8.7
def make_album(person,song,number=""):
    album={'person':person,'song':song,'number':number}
    return album
album=make_album('Roma','song1')
print(album['song'],album['person'])
album=make_album('Vlad','song2')
print(album['song'],album['person'])
album=make_album('olena','song3')
print(album['song'],album['person'])
album=make_album('busa','song4','8')
print(album['song'],album['person'],album['number'])
#8.8
while True:
    Person=input('enter person :')
    Song=input('enter song :')
    album=make_album(Person,Song)
    print(album['song'],album['person'])
    break
#8.9 and 8.10
def show_magicians(shows):
    for show in shows :
        print(show)
def make_great(mans):
    mangreat=[]
    for man in mans:
        man='Great '+man
        mangreat.append(man)
    return mangreat
y=['roma','vlad']
show_magicians(y)
print(make_great(y))
#8.11
show_magicians(y)
#8.12
def sandwich(*ingredients):
    for ingredient in ingredients:
        print(ingredient)
sandwich('bread','chiken','tomato','cucumber','cabbage')
#8.13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key] = value
    return profile
profile={}
profile=build_profile('Roma','Trotsyuk',age='18',pet='cat')
print( 'first_name :' ,profile['first_name'])
print( 'last_name :',profile['last_name'])
print('age :',profile['age'])
print('pet:',profile['pet'])
#8.14
def car_maker(Brand,model,**other):
    car={}
    car['Brand']=Brand
    car['Model']=model
    for key,value in other.items():
        car[key]=value
    return car
car = car_maker('subaru', 'outback', color='blue', tow_package=True)
print(car)
