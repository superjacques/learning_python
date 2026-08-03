# test
num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))
num3 = 1+2j
print(num3, 'is of type', type(num3))

num1 = 1; num2 = 2
print("Sum is: ",num1+num2)

languages = ["Swift", "Java", "Python", 123]
print(languages[2])
print(type(languages[3]))

#List:
#languages[2] = "Crazy"
#print(languages[2])
#languages[2] = 123
#print(languages[2])

#tuple  - immutable
product = ("Xbox", 499.99)
print(type(product))
print(product[0])

#product[0] = 123
#product[0] = "random text" #error

#collections
student_id = {112, 124, 112}
print(student_id)

#dictionary
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London', 'Nepal': 'abc'}

print(capital_city["Nepal"])

#implicit conversion
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value:",new_number)
print("Data Type:",type(new_number))

#explicit conversion:
num_string = '12'
num_integer = 23
print("Data type of num_string before casting:",type(num_string))

num_string = int(num_string) #explicit
print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string
print("Sum:",num_sum)
print("Data type new:", type(num_sum))


print("\\")
print("My name is", "Python.", end=" ")
print("Monty Python.")

#num = input("enter a number: ") ; print("You entered: ", num)
#num = int(num)
#print("Data type : " , type(num))

print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print(10 / 3)
print(10 // 3) # whole number without the remainder
print(7 % 2.5) # only the remainder, e.g. 2
print(10 ** 3) # power

#octal / hex
print(0o123)
print(0x123)

a = 5; b = 6
print((a > 4) and (b >= 6))







