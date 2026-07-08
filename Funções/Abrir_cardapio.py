import tkinter as tk
from tkinter import ttk
from Funções.Abrir_menu_de_sabores import criar_pizza
from Classes.pizza import calabresa, frango
import Imagens

def abrir_cardapio():
    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x600")
    cardapio.minsize(400, 300)
    cardapio.configure(bg="Brown")

    inicio = tk.Frame(cardapio)
    inicio.pack()
    titulo = tk.Label(inicio,
     text="Cardápio",
     font=("", 30, "bold", "italic"),
     bg= "brown")
    titulo.pack()

    FrameCalabresa = tk.Frame(cardapio,
     bg="Red",
     width= 100,
     height= 100,
     bd= 8,
     relief= "sunken")
    FrameCalabresa.pack()

    imagem_calabresa = cardapio.imagem_calabresa = tk.PhotoImage(file="Imagens/Calabresa.png")
    cardapio.imagem_calabresa = cardapio.imagem_calabresa.subsample(3, 3)

    #Radiobuttons
    PizzaEscolhida = tk.StringVar(value="")
    tk.Radiobutton(FrameCalabresa,
     text=f"{calabresa.sabor}\n{calabresa.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_calabresa,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Calabresa").pack(padx= 200)







    

    