#assignment 3 
#ques no. 1(user inputs in the list)
l=[]
num1=input('enter first number')
num2=input('enter second number')
num3=input('enter third number')
num4=input('enter forth number')
l.append(num1)
(l.append(num2)
l.append(num3)
l.append(num4)
print(l)

#ques no. 2
l.append("facebool")
l.append("google")
l.append("tesla")
l.append("microsoft")
print(l)

#ques no. 3
#syntax;-
#l.count(obj)
l.count("facebool")
l.count("googlr")

#ques no. 4
a=[3,5,2,6,3,66,34,64,2]
a.sort()
print(a)
#result
#[2, 2, 3, 3, 5, 6, 34, 64, 66]

#ques no.5
a=[123,234,231,22]
a.sort()
b=[22,33,22,11,89]
b.sort()
c=a+b
print(c)
#[22, 123, 231, 234, 11, 22, 22, 33, 89]
c.sort()
print(c)
#[11, 22, 22, 22, 33, 89, 123, 231, 234]
 






#ques no. 6
l=[1,2,3,4,5]
l.append("6")
print(l)
print(l.pop())
print('as a stack:',l)
#
l=[1,2,3,4,5]
l.append("6")
print(l)
del l[0]
print('as a queue:',l)
