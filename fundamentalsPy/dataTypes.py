# List ---------------------------------------------
# Declaration
myList = [0.2, 1, 'data', {x:2}]
print(myList)
otherList = ['a', 'b', 'c']
# Methods
# Add element in the end of list
myList.append('my name is tito bambino')
print(myList)
# add a list to my list 
myList.extend(otherList);
print(myList)

# Tuplas ---------------------------------------------
# tuplas are immutables:
# - Reserva de memoria igual => más eficiente
# Declaration
myTupla = 0.2, 2, 'tup', 'hola'

# Set ---------------------------------------------
# no repeat elements:
# the order not be care
# Declaration
mySet = {0.7, 5, 'setsi', 'adios', 'setsi'} # to verify
# Conver
s = set('fresa')
o = set('mandarina')
print(s) 
# operations between sets
# s - o => difference
# s | o => bot sets
# s & o =>  sets
# s ^ o => elements of bot sets but not the same elements

# dictionary ---------------
# declaration
myHash = {'andres', 123; 'raul', 431}
# lenght
print(len myHash)
# delete
del myHash['andres']
# has
print('raul' in myHash)
# values
print()
# pop 






