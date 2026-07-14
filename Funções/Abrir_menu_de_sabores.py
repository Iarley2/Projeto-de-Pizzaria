import tkinter as tk
from tkinter import ttk
from Classes.pizza import Pizza, calabresa, frango, queijo, portuguesa, margherita, napolitana


def abrir_menu():
    Menu = tk.Toplevel()
    Menu.title("Menu de Sabores")
    Menu.geometry("800x600")
    Menu.minsize(400, 300)
    Menu.configure(bg= "Brown",  bd= 10, relief="sunken")

    canvas = tk.Canvas(Menu, bg="Brown", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(Menu, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    conteudo = tk.Frame(canvas, bg="Brown")
    canvas.create_window((0, 0), window=conteudo, anchor="nw")

    conteudo.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    criar_pizza(conteudo, calabresa, "Imagens/Calabresa.png")
    criar_pizza(conteudo, frango, "Imagens/Frango.png")
    criar_pizza(conteudo, queijo, "Imagens/Queijo.png")
    criar_pizza(conteudo, portuguesa, "Imagens/Portuguesa.png")
    criar_pizza(conteudo, margherita, "Imagens/Margherita.png")
    criar_pizza(conteudo, napolitana, "Imagens/Napolitana.png")

def criar_pizza(janela, pizza, imagem): #Janela que fica | Pizza = objeto
     frame = tk.Frame(janela, bd= 10, relief="sunken", bg= "Red")
     frame.pack(fill="x")

     nome = tk.Label(frame,
        text=f"Sabor: {pizza.sabor}\n {pizza.mostrar_ingredientes()} \n Preço R$: {pizza.valor_inicial}",
        font=("", 20, "bold", "italic"), 
        bd= 4, 
        relief= "sunken")
     nome.pack()

     foto = tk.PhotoImage(file=imagem)
     foto = foto.subsample(3, 3)

     label = tk.Label(frame, image=foto, bd=4, relief="sunken")
     label.image = foto
     label.pack()
     


    