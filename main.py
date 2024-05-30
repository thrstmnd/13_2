import tkinter as tk
from tkinter import messagebox
import wikipedia

root = Tk()
def facts():
    city = entry.get()
    page = wikipedia.page(city)
    fact1 = page.summary.split('\n')[0]
    fact2 = page.summary.split('\n')[1]
    messagebox.showinfo("Исторические факты - {}".format(city), "{}\n{}".format(fact1, fact2))
    
root.geometry("300x300")
root.title("Города")

label = Label(root, text="Введите название города:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Найти факты", command=facts)
button.pack()

root.mainloop()
