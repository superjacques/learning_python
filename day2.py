"""
day 2


Reminder from day1:
✅ List       Ordered, changeable, duplicates allowed ... []
✅ Tuple      Ordered, fixed, duplicates allowed      ... ()
✅ Set        Unordered, unique values only           ... {}
✅ Dictionary Key-value pairs, keys must be unique    ... {abc:xyz, def:fgh}
| Container      | Best used for                    | Example                                                 |
| -------------- | -------------------------------- | ------------------------------------------------------- |
| **List**       | A collection that changes        | Shopping list, students, tasks                          |
| **Tuple**      | Fixed data that shouldn't change | GPS coordinate `(33.9, 25.6)`, RGB colour `(255, 0, 0)` |
| **Set**        | Unique items only                | Employee IDs, tags, permissions                         |
| **Dictionary** | Look up a value by a key         | Person → phone number, product → price                 |
"""

age = 18    #if/ else ... choose two paths
if age >= 18:   print("Adult")
else:           print("Child")

print("For loop")  #repeats the code
for number in range(3):
    print(number)

c= 5
for i in range(0, c): print(i)

print("While loop:")  #repeats while the condition stays true
count = 0
while count < 3:
    print(count)
    count += 1
    
print("Break") #stops the loop compltely
for number in range(10):
    if number == 5:
        break
    
print("Continue") #skips current round and goes to the next
for number in range(5):
    if number == 2:
        continue
    print(number)

#pass does nothing. placeholder
if age >= 18:
    pass

print("if elif else") #if / elif / else
mark = 78
if mark >= 80:
    print("Distinction")
elif mark >= 65:
    print("Very good!")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")

#Nested if/else
age = 18 ; has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Fetch your ID")
else:
    print("Too young")

age = 60
a = "Adult" if age >= 50 else "Child"
print(a)


##Iterate through a list
mylist = ["python","is","great"]
for i in range(len(mylist)): print(mylist[i])

##Iterate through a list
mylist = ["python","is","great"]
for i in range(len(mylist)): print("I love python")







