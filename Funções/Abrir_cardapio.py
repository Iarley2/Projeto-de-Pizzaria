import tkinter as tk
from tkinter import ttk
from Funções.Abrir_menu_de_sabores import criar_pizza
from Classes.pizza import calabresa, frango
from Classes.Cliente import Pessoa
import Imagens

def abrir_cardapio(cliente):

    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x800")
    cardapio.minsize(400, 300)
    cardapio.configure(bg="Brown")

    acoes = tk.Frame(cardapio, bg="Red")
    acoes.pack(pady= 20)

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

    FrameFrango = tk.Frame(cardapio,
     bg="Green",
     width= 100,
     height= 100,
     bd= 8,
     relief= "sunken")
    FrameFrango.pack()

    #Radiobuttons
    imagem_calabresa = cardapio.imagem_calabresa = tk.PhotoImage(file="Imagens/Calabresa.png")
    cardapio.imagem_calabresa = cardapio.imagem_calabresa.subsample(3, 3)

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
    
    imagem_frango = cardapio.imagem_frango = tk.PhotoImage(file= "Imagens/Frango.png")
    cardapio.imagem_frango = cardapio.imagem_frango.subsample(3, 3)

    tk.Radiobutton(FrameFrango,
     text=f"{frango.sabor}\n{frango.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_frango,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Frango").pack(padx= 200)
    
    #botão final
    acoes = tk.Frame(cardapio,
     bg= "Brown")
    acoes.pack(pady= 20)

    def finalizar_pedido():
     escolha = PizzaEscolhida.get()
     cliente.cadastrar(escolha)
     cardapio.destroy()


    finalizar = tk.Button(acoes,
     text="Finalizar pedido",
     bg= "Red", 
     command = finalizar_pedido, 
     font= ("", 20, "bold"), 
     bd= 10, 
     relief= "sunken")
    finalizar.pack(pady= 20)
    







    

    