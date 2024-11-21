import pprint

import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.02f} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


"""
response = requests.get('https://open.er-api.com/v6/latest/USD')
response.raise_for_status()
data = response.json()

p = pprint.PrettyPrinter(indent=4)
p.pprint(data)
"""

window = Tk()
window.title("EXCHANGE")
window.geometry("360x180")
window.configure(background='white')
window.configure(highlightbackground='white')

label = Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry(window)
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()