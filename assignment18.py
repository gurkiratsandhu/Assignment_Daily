#1.

import tkinter
from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("Helvetica", 12),yscrollcommand=w.set)



d={"bikram":999,"rajat":895,"vijay":567,"vivek":5658,"ekta":6576,"deepa":45747,"divya":5345,"surya":45678,"poonam":4586,"diskha":809687}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)
root.mainloop()






#2.
import tkinter
from tkinter import *

def show():
    k=entry.get()
    v=entry2.get()
    mylist.insert(END,'{}: {}'.format(k, v))
    d[k]=v
    print(d)

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("MT Bold", 12),yscrollcommand=w.set)



d={"gayatri":999,"astha":895,"niku":567,"harpreet":5658,"bhuvi":6576,"geetu":45747,"rohit":5345,"kamini":45678,"ram":4586,"sahil":809687}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)

entry=Entry(root,width=20)
entry.pack()
entry2=Entry(root,width=20)
entry2.pack()
b=Button(root,text="insert",bg="pink",command=show)
b.pack()
root.mainloop()