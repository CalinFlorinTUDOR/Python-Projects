import tkinter as tk

root = tk.Tk()

root.geometry('600x500')
root.title('Kalidevi first GUI')

label = tk.Label(root, text='Hello World!', font=('Ubuntu Condensed', 18))
label.pack(padx=15, pady=30)

textbox = tk.Text(root, height=4, font=('Ubuntu Condensed', 15))
textbox.pack(padx=7, pady=7)


myentry = tk.Entry(root)
myentry.pack()


# button = tk.Button(root, text='Push the button', font=('Ubuntu Condensed', 15))
# button.pack(padx=7, pady=7) # when you need to add  just one button

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Ubuntu Condensed', 16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Ubuntu Condensed', 16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Ubuntu Condensed', 16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Ubuntu Condensed', 16))
btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Ubuntu Condensed', 16))
btn5.grid(row=1, column=0, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Ubuntu Condensed', 16))
btn6.grid(row=1, column=1, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('Ubuntu Condensed', 16))
btn7.grid(row=1, column=2, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('Ubuntu Condensed', 16))
btn8.grid(row=1, column=3, sticky=tk.W+tk.E)
buttonframe.pack(fill='x')


anotherbtn = tk.Button(root, text='Submit')
anotherbtn.place(x=265, y=305, height=70, width=70)

root.mainloop()