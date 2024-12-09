#variables 
age =20
temperature = 25.39
country = "Australia"
is_day = True;

#allows us to display messages to console.
print(country)

#variables are not set in stone and can be changed.
country = "Ireland"

print(country)
#somthing has to be in the variable before it can be used.
#or it will error.

#you can change the type of varible as well
country = 900

print(country)

country_name = "England"
population = 2000
landlocked = False
border_size = 20.50

#operators
health = 100
damage = 20
health = health - damage
health = health + 50
health = health * 1.5
health = health / 2

a = 5
b = 8

#if statement
if a == b:
    print('a is equal to b')

#if else statement
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")    

#else if
name = "Bob"

if name  == "Jack":
    print ("you are Jack")
elif name == "Bob":
    print("You are Bob")
else:
    print("You are not Jack or Bob")

#Functions
#a function is a block of reusable code

print("hello Bob")
print("hello Steve")
print("hello Mary")

def say_hello (name):
    print("Hello " + name)

say_hello("Andrew")