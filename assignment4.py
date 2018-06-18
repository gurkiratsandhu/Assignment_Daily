#assignment no.4
#ques no. 1
tuple=(1,2,"hello")
a=len(tuple)
print(a)
# ques  no. 2
a=max(tuple)
print(a)
# ques no. 3
# Python program to multiply all values in the
# list using traversal
 
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 
     
# Driver code
list1 = [1, 2, 3] 
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
# **************************************************************************
#***************************************************************************
#sets***********************************************************************
#ques no. 1
aa=set()
num1=input("enter 1st value")
num2=input("enter 2nd value")
num3=input("enter 3rd value")
aa.update([num1,num2,num3])
print(aa)
#ques 2
ds={1,23,4}
sd={23,4}
e=ds.difference(sd)
print(e)
#ques 3
q=ds.intersection(sd)
print(q)
#ques 4