# Simple Calculator Program
from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


main = Tk()
main.title("Simple Calculator program")
main.geometry("400x400")
main.configure(bg='black')

equation_text = ""

equation_label = StringVar()

label = Label(main, textvariable=equation_label, font=('consolas',14), bg="white", width=20, height=2)
label.pack(pady=5)

frame = Frame(main)
frame.pack()

tombol0 = Button(frame, text=0, height=3, width=8, font=30, command=lambda: button_press(0))
tombol0.grid(row=3, column=1)

tombol1 = Button(frame, text=1, height=3, width=8, font=30, command=lambda: button_press(1))
tombol1.grid(row=2, column=0)

tombol2 = Button(frame, text=2, height=3, width=8, font=30, command=lambda: button_press(2))
tombol2.grid(row=2, column=1)

tombol3 = Button(frame, text=3, height=3, width=8, font=30, command=lambda: button_press(3))
tombol3.grid(row=2, column=2)

tombol4 = Button(frame, text=4, height=3, width=8, font=30, command=lambda: button_press(4))
tombol4.grid(row=1, column=0)

tombol5 = Button(frame, text=5, height=3, width=8, font=30, command=lambda: button_press(5))
tombol5.grid(row=1, column=1)

tombol6 = Button(frame, text=6, height=3, width=8, font=30, command=lambda: button_press(6))
tombol6.grid(row=1, column=2)

tombol7 = Button(frame, text=7, height=3, width=8, font=30, command=lambda: button_press(7))
tombol7.grid(row=0, column=0)

tombol8 = Button(frame, text=8, height=3, width=8, font=30, command=lambda: button_press(8))
tombol8.grid(row=0, column=1)

tombol9 = Button(frame, text=9, height=3, width=8, font=30, command=lambda: button_press(9))
tombol9.grid(row=0, column=2)

plus = Button(frame, text='+', height=3, width=8, font=30, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=3, width=8, font=30, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=3, width=8, font=30, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=3, width=8, font=30, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=3, width=8, font=30, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=3, width=8, font=30, command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

clear = Button(main, text='clear', height=2, width=8, font=30, command=clear)
clear.pack(pady=5)

main.mainloop()