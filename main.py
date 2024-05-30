import tkinter as tk
from tkinter import messagebox
import wikipedia

def show_facts():
    city = entry.get()
    try:
        page = wikipedia.page(city)
        fact1 = page.summary.split('\n')[0]
        fact2 = page.summary.split('\n')[1]
        messagebox.showinfo("Исторические факты - {}".format(city), "{}\n{}".format(fact1, fact2))
    except wikipedia.exceptions.PageError:
        messagebox.showinfo("Ошибка", "Информация о данном городе отсутствует в базе данных.")

root = tk.Tk()
root.geometry("300x300")
root.title("Города")

label = tk.Label(root, text="Введите название города:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Найти факты", command=show_facts)
button.pack()

root.mainloop()