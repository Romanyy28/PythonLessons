#3.1
names=['Ivan','Victor','Vlad']
print('Hello ',names[0],' would you like join me and ',names[1], 'to go to ',names[2])
#3.2
print('Hi',names[0],'would you like go to walk ?')
print('Hi',names[1],'would you like go to walk ?')
print('Hi',names[2],'would you like go to walk ?')
#3.3
cars=['Audi','BMW','Volvo']
print('I would like bye a car , it can be :',cars)
#3.4
list=['Ivan','Victor','Vlad']
print('Dear',list[0],'I invite you to dinner at 14 am')
print('Dear',list[1],'I invite you to dinner at 14 am')
print('Dear',list[2],'I invite you to dinner at 14 am')
#3.5
print('Can not be ',list[0])
list[0]='Roma'
print('Dear',list[0],'I invite you to dinner at 14 am')
print('Dear',list[1],'I invite you to dinner at 14 am')
print('Dear',list[2],'I invite you to dinner at 14 am')
#3.6
print('New guests :') 
list.insert(0,'Olena')              
list.insert(2,'Busa')
list.append('Tanya')
print('Dear',list[0],'I invite you to dinner at 14 am')
print('Dear',list[1],'I invite you to dinner at 14 am')
print('Dear',list[2],'I invite you to dinner at 14 am')
print('Dear',list[3],'I invite you to dinner at 14 am')
print('Dear',list[4],'I invite you to dinner at 14 am')
print('Dear',list[5],'I invite you to dinner at 14 am')
#3.7
print('just 2 guests')
print('Sorry',list[5])
list.pop(5)
print('Sorry',list[4])
list.pop(4)
print('Sorry',list[3])
list.pop(3)
print('Sorry',list[2])
list.pop(2)
print('Dear',list[0],'I invite you to dinner at 14 am')
print('Dear',list[1],'I invite you to dinner at 14 am')
#3.8
country=['italy','usa','turkey','japan']
print(country)
print(sorted(country))
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
#3.9
print(len(list))
#3.10
family=['mam','dad','brother','sister','me']
print(family)
print(family[0])
family.pop(4)
print(sorted(family))
family.reverse()
family.sort()
family[-1]