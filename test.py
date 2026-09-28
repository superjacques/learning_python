import copy
fruits = [["Apple", "Mango"], ["Banana", 'Orange']]
newlist = fruits.deepcopy()
newlist[0][1]='Kiwi'
print(fruits)
print(newlist)