import tkinter as tk
from tkinter import font

def show_output():
    number = int(number_input.get())

    if number == 0 :
        output_label.configure(text='เป็น0ไม่ได้นะ')
        return

    output = ''
    for i in range (1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)


window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400,height=400)

FONT1 = ('Angsana New' , 20)

title_label = tk.Label(master=window,text='สูตรคูณแม่',font=FONT1,)
title_label.pack(pady=20)

number_input = tk.Entry(master=window,width=20,font=FONT1)
number_input.pack(pady=10)

go_button = tk.Button(master=window, text='ได้แก่',command=show_output,
                        width=15,height=2)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()