#Q.1- What is Time Tuple?
import time
print(time.gmtime())

#Q.2- Write a program to get formatted time.
import time
print(time.asctime())

#Q.3- Extract month from the time.
import datetime
d=datetime.date.today()
print(d.month)

#Q.4- Extract day from the time.
import datetime
d=datetime.date.today()
print(d)
print(d.day)

#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
d=datetime.date.today()
print(d.month)

#Q.6- Write a program to print time using localtime method.
import time
print(time.localtime())

#Q.7- Find the factorial of a number input by user using math package functions.
import math
print(math.factorial(4))

#Q.8- Find the GCD of a number input by user using math package functions.
import math
a=int(input("enter a value: "))
b=int(input("enter b value: "))
print(math.gcd(a,b))

#Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.
import os
print(os.getcwd())
print(os.environ)