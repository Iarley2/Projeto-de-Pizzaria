import tkinter as tk
from tkinter import ttk

def abrir_cardapio():
    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x600")
    cardapio.minsize(400, 300)

    inicio = ttk.Frame(cardapio, padding=30)
    inicio.pack()
    titulo = ttk.Label(titulo,
     text="Cardápio",
     font=("",20, "bold"))
    