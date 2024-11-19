import tkinter as tk


def add():
    result_entry.delete(0, 'end')
    result_entry.insert(0, int(number1_entry.get())+int(number2_entry.get()))


def sub():
    result_entry.delete(0, 'end')
    result_entry.insert(0, int(number1_entry.get())-int(number2_entry.get()))


def mul():
    result_entry.delete(0, 'end')
    result_entry.insert(0, int(number1_entry.get())*int(number2_entry.get()))


def div():
    result_entry.delete(0, 'end')
    if int(number2_entry.get()) == 0:
        return
    result_entry.insert(0, int(number1_entry.get())/int(number2_entry.get()))


window = tk.Tk()
window.title('Kalkulator')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', command=add).place(x=50, y=165)
button_sub = tk.Button(window, text='-', command=sub).place(x=100, y=165)
button_mul = tk.Button(window, text='*', command=mul).place(x=150, y=165)
button_sub = tk.Button(window, text='/', command=div).place(x=200, y=165)

label1_label = tk.Label(text='Введите первое число:').place(x=50, y=50)
number1_entry = tk.Entry()
number1_entry.place(x=50, y=75)
label2_label = tk.Label(text='Введите второе число:').place(x=50, y=110)
number2_entry = tk.Entry()
number2_entry.place(x=50, y=135)
label3_label = tk.Label(text='Результат:').place(x=50, y=200)
result_entry = tk.Entry()
result_entry.place(x=50, y=225)

window.mainloop()
