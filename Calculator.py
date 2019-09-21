from tkinter import *
import parser

root = Tk()
root.title("Prakher's Calci")
root.geometry('308x279')
root.configure(background="sky blue")

operator = ""
texin = StringVar()

def values(number):
    global operator
    operator = operator+str(number)
    texin.set(operator)

def equal():
    global operator
    result = eval(operator)
    texin.set(result)
    operator= str(result)

def clear():
    global operator
    operator= ""
    texin.set(operator)



label1 = Label(root,text="CALCULATOR",font=("Helvetica",10, 'bold'), bg="sky Blue")
label1.grid(row=0,columnspan=5)

display = Entry(root, font=('Verdana',18), textvar=texin)
display.grid(rowspan =3,columnspan=5,sticky = W+E)

Button(root, text='7', width=3,padx=14, pady=14,bd=4, command=lambda:values(7)).grid(row= 4, column=0)
Button(root, text='8',width=3,padx=14, pady=14,bd=4, command=lambda:values(8)).grid(row= 4, column=1)
Button(root, text='9', width=3,padx=14, pady=14,bd=4, command=lambda:values(9)).grid(row= 4, column=2)
Button(root, text='/', width=3,padx=14, pady=14,bd=4, command=lambda:values("/")).grid(row= 4, column=3)
Button(root, text='Clear', width=3,padx=15, pady=14,bd=4, command=lambda:clear()).grid(row= 4, column=4)

Button(root, text='4', width=3,padx=14, pady=14,bd=4, command=lambda:values(4)).grid(row= 5, column=0)
Button(root, text='5', width=3,padx=14, pady=14,bd=4, command=lambda:values(5)).grid(row= 5, column=1)
Button(root, text='6', width=3,padx=14, pady=14,bd=4, command=lambda:values(6)).grid(row= 5, column=2)
Button(root, text='*', width=3,padx=14, pady=14,bd=4, command=lambda:values("*")).grid(row= 5, column=3)
Button(root, text='exp', width=3,padx=15, pady=14,bd=4, command=lambda:values("**")).grid(row= 5, column=4)

Button(root, text='1', width=3,padx=14, pady=14,bd=4, command=lambda:values(1)).grid(row= 6, column=0)
Button(root, text='2', width=3,padx=14, pady=14,bd=4, command=lambda:values(2)).grid(row= 6, column=1)
Button(root, text='3', width=3,padx=14, pady=14,bd=4, command=lambda:values(3)).grid(row= 6, column=2)
Button(root, text='-', width=3,padx=14, pady=14,bd=4, command=lambda:values("-")).grid(row= 6, column=3)

Button(root, text='0', width =9,padx=23, pady=14,bd=4, command=lambda:values(0)).grid(row= 7, columnspan=2)
Button(root, text='.', width=3,padx=14, pady=14,bd=4, command=lambda:values(".")).grid(row= 7, column=2)
Button(root, text='+', width=3,padx=14, pady=14,bd=4, command=lambda:values("+")).grid(row= 7, column=3)
Button(root, text='=', width=3, height=4, padx=14, pady=17,bd=6, command=lambda:equal()).grid(row= 6, rowspan=2, column=4)
root.mainloop()
