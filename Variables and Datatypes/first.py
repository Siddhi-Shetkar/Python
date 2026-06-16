print("Hello World!")
print("My name is Siddhi", "My age is 20")
print(34)
name="Arya"
age=19
print("My friends name is "+name)
print("My friends age is ", age)
price  =25.99
print(type(price))

name1="sk"
name2='sk'
name3="""sk"""
name4='''sk'''
print(name1,name2,name3,name4)

a=None
print(type(a))

b = 2
c = 5
sum = b+c
print(sum)

# arithmetic operations
x = 34
y =45
print("Addition of x and y is ", x+y)
print("Subtraction of x and y is ", x-y)
print("Multiplication of x and y is ", x*y)
print("Division of x and y is ", x/y)
print("Modulus of x and y is ", x%y)
print("Exponentiation of x and y is ", x**y)

# relational operators
if(x!=y):
    print("x is not equal to y")

print(x==y)

# assignment operators
x+=10
print(x)
x*=5
print(x)
x/=2
print(x)

# logical operators
print(not False)
print(not (x>y))

val1 = True
val2 = False
print(val1 and val2)
print(val1 or val2)

# type conversion
num1 = 10
num2 = 20.5
print(num1+num2)

# type casting
n="2"
m=5
p = int(n)
total = p+m
print(total)

# take user input
name = input("Enter your name: ")
print("Welcome", name)

# by default
val = input("Enter customer name: ")
print(type(val), val) #if i enter a number also it will be considered as string

# we need to type cast
val = int(input("Enter customer age: "))
print(type(val), val) #if i enter a number it will be considered as integer