import tkinter as tk
from tkinter import ttk

def abrir_cardapio():
    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x600")
    cardapio.minsize(400, 300)

    titulo= ttk.Frame(cardapio, padding=30)
    mensagem2= ttk.Label(titulo, text="Cardápio")
    mensagem2.pack()