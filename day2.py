"""
day 2
"""
age = 18    #if/ else ... choose two paths
if age >= 18:   print("Adult")
else:    		print("Child")

print("For loop")  #repeats the code
for number in range(3):
    print(number)

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