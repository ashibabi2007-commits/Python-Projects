from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

root=Tk()
root.title("Calculator")
root.geometry("328x438")
root.maxsize(328,438)
root.configure(background="black")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    result_label.config(text=expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        result_label.config(text=result)
        expression = result
    except:
        result_label.config(text="Wrong")
        expression = ""

def clear():
    global expression
    expression = ""
    result_label.config(text="0")

result_label=Label(root,text='0',bg='black',fg='white')
result_label.grid(row=0,column=0,sticky='e',columnspan=800)
result_label.config(font=('verdina',20))



button9=Button(root,text='9',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(9))
button9.grid(row=1,column=0)
button9.config(font=('verdana',19,'bold'))

button8=Button(root,text='8',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(8))
button8.grid(row=1,column=1)
button8.config(font=('verdana',19,'bold'))

button7=Button(root,text='7',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(7))
button7.grid(row=1,column=2)
button7.config(font=('verdana',19,'bold'))

#sum
buttonsum=Button(root,text='+',bg="darkblue",fg='white',width=4,height=2,command=lambda:press('+'))
buttonsum.grid(row=1,column=3)
buttonsum.config(font=('verdana',19,'bold'))

button6=Button(root,text='6',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(6))
button6.grid(row=2,column=0)
button6.config(font=('verdana',19,'bold'))

button5=Button(root,text='5',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(5))
button5.grid(row=2,column=1)
button5.config(font=('verdana',19,'bold'))

button4=Button(root,text='4',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(4))
button4.grid(row=2,column=2)
button4.config(font=('verdana',19,'bold'))

button3=Button(root,text='3',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(3))
button3.grid(row=3,column=0)
button3.config(font=('verdana',19,'bold'))

#sub
buttonsub=Button(root,text='-',bg="darkblue",fg='white',width=4,height=2,command=lambda:press('-'))
buttonsub.grid(row=2,column=3)
buttonsub.config(font=('verdana',19,'bold'))

button2=Button(root,text='2',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(2))
button2.grid(row=3,column=1)
button2.config(font=('verdana',19,'bold'))

button1=Button(root,text='1',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(1))
button1.grid(row=3,column=2)
button1.config(font=('verdana',19,'bold'))

#mul
buttonmult=Button(root,text='x',bg="darkblue",fg='white',width=4,height=2,command=lambda:press('*'))
buttonmult.grid(row=3,column=3)
buttonmult.config(font=('verdana',19,'bold'))

button0=Button(root,text='0',bg="#ff9d00",fg='white',width=4,height=2,command=lambda:press(0))
button0.grid(row=4,column=1)
button0.config(font=('verdana',19,'bold'))

#can
buttoncan=Button(root,text='C',bg="darkblue",fg='white',width=4,height=2,command=clear)
buttoncan.grid(row=4,column=0)
buttoncan.config(font=('verdana',19,'bold'))

#equal
buttoneq=Button(root,text='=',bg="darkblue",fg='white',width=4,height=2,command=equal)
buttoneq.grid(row=4,column=2)
buttoneq.config(font=('verdana',19,'bold'))

#div
buttondiv=Button(root,text='/',bg="darkblue",fg='white',width=4,height=2,command=lambda:press('/'))
buttondiv.grid(row=4,column=3)
buttondiv.config(font=('verdana',19,'bold'))






root.mainloop()