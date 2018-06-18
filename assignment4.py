#assignment4
#Q.1- Write a program to create a tuple with different data types and do the following operations. 
#1. Find the length of tuples
t=(2,4,3,'a',2.5)
print(t)
print(len(t))


#Q.2-Find largest and smallest elements of a tuples. 
t=(8,9,2,7,1)
print(t)
print(max(t))
print(t)
print(min(t)
print(t)

#Q.3- Write a program to find the product of all elements of a tuple.
t=(1,2,3)
p=1
p=p*t[0]
p=p*t[1]
p=p*t[2]
print(p)

#sets
#Q.1- Create two set using user defined values. 
#1. Calculate difference between two sets.
s1={1,2,3}
s2={6,2,4}
print(s1-s2)

#2. Compare two sets.
s1{1,2,3}
s2{1,4,5}
print(s1^s2)

#3. Print the result of intersection of two sets.
s1{1,2,3}
s2{1,4,5}
print(s1&s2)

#dictionary
#Q.1- Create a dictionary to store name and marks of 10 students by user input. 
name=input("enter name: ")
a=int(input("enter marks: "))

name=input("enter name: ")
b=int(input("enter marks: "))

name=input("enter name: ")
c=int(input("enter marks: "))

name=input("enter name: ")
d=int(input("enter marks: "))

name=input("enter name: ")
e=int(input("enter marks: "))

name=input("enter name: ")
f=int(input("enter marks: "))

name=input("enter name: ")
g=int(input("enter marks: "))

name=input("enter name: ")
h=int(input("enter marks: "))

name=input("enter name: ")
i=int(input("enter marks: "))

name=input("enter name: ")
j=int(input("enter marks: "))

d=[a,b,c,d,e,f,g,h,i,j]
print(d)

#Q.2-Sort the dictionary created in previous question according to marks.
name=input("enter name: ")
a=int(input("enter marks: "))

name=input("enter name: ")
b=int(input("enter marks: "))

name=input("enter name: ")
c=int(input("enter marks: "))

name=input("enter name: ")
d=int(input("enter marks: "))

name=input("enter name: ")
e=int(input("enter marks: "))

name=input("enter name: ")
f=int(input("enter marks: "))

name=input("enter name: ")
g=int(input("enter marks: "))

name=input("enter name: ")
h=int(input("enter marks: "))

name=input("enter name: ")
i=int(input("enter marks: "))

name=input("enter name: ")
j=int(input("enter marks: "))

d=[a,b,c,d,e,f,g,h,i,j]
print(d.sort())
print(d)

#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
l=list("MISSISSIPPI")
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['P']=l.count('P')
print(d)