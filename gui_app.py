#graphic user interface

#libraries
# 1.Tkinter
# 2.Turtle
# 3.pyQT

#from socket import MsgFlag
import tkinter as ttk
from unittest import result

app = ttk.Tk()
app.title('My App')
app.geometry('600x400')
ttk.Label(app,text='A simle text Label').grid(column =0,rows =4)
ttk.Label(app,text=" machine learning ").place(x=50,y=50)

msg = ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())

def abc():
    print("wow")
    msg.set("data changed")

ttk.Button(app, text="click it",command = abc).\
     place(x=100,y=100)
ttk.Button(app, text= "this one",command = lambda:msg.set("again setted")).\
    place(x=100,y=130)


f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result= ttk.Variable(app)


ttk.Entry(app, textvariable = f1 ,fg='blue', font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app, textvariable = f2 , fg='blue',font=('Arial',22)).place(x=150,y=200)
ttk.Label(app,text="result").place(x=100,y=300)
ttk.Label(app,textvariable= result ,font =('Arial',22)).place(x=100,y=330)

def calci(op):
    print("i will calculate")
    result.set(eval(f1.get()+op + f2.get()))
    

ttk.Button(app, text = '+' , command = lambda : calci('+'), font=('Arial',22)).\
    place(x=50, y=240)
ttk.Button(app, text = '-' , command = lambda: calci('-'), font=('Arial',22)).\
    place(x=100, y=240)
ttk.Button(app, text = '*' , command =lambda: calci('*'), font=('Arial',22)).\
    place(x=150, y=240)
ttk.Button(app, text = '/' , command =lambda : calci('/'), font=('Arial',22)).\
    place(x=200, y=240)

#list box widget

box = ttk.Listbox(app,height = 7, fg ='orange',bg ='blue', activestyle='dotbox')
box.insert(1, 'sample1')
box.insert(2, 'sample2')
box.insert(3, 'sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app,text='show',command=show).place(x=350,y=250)

app.mainloop()