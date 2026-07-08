import tkinter as tk
from tkinter import ttk
from Classes.pizza import Pizza, calabresa


def abrir_menu():
    Menu = tk.Toplevel()
    Menu.title("Menu de Sabores")
    Menu.geometry("800x600")
    Menu.minsize(400, 300)

    """pizza_de_calabresa = ttk.Frame(Menu, padding= 20)
    pizza_de_calabresa.pack()

    nomeCalabresa = ttk.Label(pizza_de_calabresa,
     text = f"Sabor: {calabresa.sabor}\n {calabresa.mostrar_ingredientes()}",
     font= ("", 20))
    nomeCalabresa.pack()

    ImagemCalabresa = tk.PhotoImage(file= "Imagens/Calabresa.png")
    ImagemCalabresa = ImagemCalabresa.subsample(3,3)
    label = tk.Label(pizza_de_calabresa, image = ImagemCalabresa, bd= 4, relief= "sunken")
    label.image = ImagemCalabresa
    label.pack()"""
    criar_pizza(Menu, calabresa, "Imagens/Calabresa.png")


def criar_pizza(janela, pizza, imagem): #Janela que fica | Pizza = objeto
     frame = ttk.Frame(janela, padding=20)
     frame.pack()

     nome = ttk.Label(frame,
        text=f"Sabor: {pizza.sabor}\n{pizza.mostrar_ingredientes()}",
        font=("", 20))
     nome.pack()

     foto = tk.PhotoImage(file=imagem)
     foto = foto.subsample(3, 3)

     label = tk.Label(frame, image=foto, bd=4, relief="sunken")
     label.image = foto
     label.pack()
     


    