from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x450")
window.config(bg="light grey")

equation_str = ""

def show_value(value):
    global equation_str
    equation_str += value
    label_display.config(text=equation_str)

def clear():
    global equation_str
    equation_str = ""
    label_display.config(text=equation_str)

def calculate_result():
    global equation_str
    result = ""
    if equation_str != "":
        try:
            result = eval(equation_str)
        except:
            result = "Error"
            equation_str = ""
        label_display.config(text=result)

label_display = Label(window, width=25, height=3, font=("Courier", 20, "underline"))
label_display.place(x=1, y=0)

Button(window, text="C", bg="red", fg="white", font=("Arial", 20, "underline"), width=5, height=1, relief=RAISED, bd=2, command=clear).place(x=10, y=110)
Button(window, text="4", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('4')).place(x=10, y=250)
Button(window, text="5", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('5')).place(x=110, y=250)
Button(window, text="6", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('6')).place(x=210, y=250)
Button(window, text="+", bg="#2a2d36", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('+')).place(x=310, y=250)
Button(window, text="/", bg="#2a2d36", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('/')).place(x=110, y=110)
Button(window, text="%", bg="#2a2d36", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('%')).place(x=210, y=110)
Button(window, text="*", bg="#2a2d36", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('*')).place(x=310, y=110)
Button(window, text="1", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('1')).place(x=10, y=320)
Button(window, text="2", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('2')).place(x=110, y=320)
Button(window, text="3", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('3')).place(x=210, y=320)
Button(window, text="=", bg="#EC7063", fg="white", font=("Arial", 20, "bold"), width=5, height=3, relief=RAISED, bd=2, command=calculate_result).place(x=310, y=323)
Button(window, text="7", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('7')).place(x=10, y=180)
Button(window, text="8", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('8')).place(x=110, y=180)
Button(window, text="9", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('9')).place(x=210, y=180)
Button(window, text="-", bg="#2a2d36", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('-')).place(x=310, y=180)
Button(window, text="0", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=11, height=1, relief=RAISED, bd=2, command=lambda: show_value('0')).place(x=10, y=390)
Button(window, text=".", bg="#B3B6B7", fg="white", font=("Arial", 20, "bold"), width=5, height=1, relief=RAISED, bd=2, command=lambda: show_value('.')).place(x=210, y=390)

window.mainloop()
