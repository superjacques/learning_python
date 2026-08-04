"""
day 2
"""
age = 18
if age >= 18:   print("Adult")
else:    		print("Child")

print("For loop")
for number in range(3):
    print(number)

print("While loop:")
count = 0
while count < 3:
    print(count)
    count += 1
    
print("Break")
for number in range(10):
    if number == 5:
        break
    
print("Continue")
for number in range(5):
    if number == 2:
        continue
    print(number)