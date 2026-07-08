import tkinter as tk
from tkinter import ttk
from Classes.pizza import Pizza
from Funções.Abrir_menu_de_sabores import criar_pizza
from Classes.pizza import calabresa, frango
import Imagens

def abrir_cardapio():
    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x600")
    cardapio.minsize(400, 300)

    inicio = ttk.Frame(cardapio, padding=30)
    inicio.pack()
    titulo = ttk.Label(inicio,
     text="Cardápio",
     font=("", 30, "bold", "italic"))
    titulo.pack()

    #Primeira pizza

    criar_pizza(cardapio, calabresa, "Imagens/Calabresa.png")
    criar_pizza(cardapio, frango, "Imagens/Frango.png")







    

    