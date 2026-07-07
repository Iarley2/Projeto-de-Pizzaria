import tkinter as tk
from tkinter import ttk

def abrir_menu():
    Menu = tk.Toplevel()
    Menu.title("Menu de Sabores")
    Menu.geometry("800x600")
    Menu.minsize(400, 300)

    pizza_de_calabresa = ttk.Frame(Menu, padding= 50)
    pizza_de_calabresa.pack()

    calabresa = tk.PhotoImage(file= "Imagens/Calabresa.png")
    label = tk.Label(pizza_de_calabresa, image = calabresa)
    label.image = calabresa
    label.pack()