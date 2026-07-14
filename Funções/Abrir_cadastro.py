import tkinter as tk
from tkinter import ttk
from Classes.Cliente import Pessoa
from Funções.Abrir_cardapio import abrir_cardapio
from Funções.cliques import contar_cliques

Cliques = 0

def abrir_cadastro():

    cadastro = tk.Toplevel()
    cadastro.title("Pedido")
    cadastro.geometry("800x600")
    cadastro.minsize(400, 300)
    cadastro.configure(bg="Red", bd= 10, relief="sunken")

    titulo = tk.Frame(cadastro, bd= 4, relief="sunken", bg="Black")
    titulo.pack(pady= 20)

    texto = ttk.Label(titulo,
     text="Pedido", font= ("", 20, "bold", "italic")).pack()
    
    campos_para_digitar = tk.Frame(cadastro, bd= 10, relief="sunken", bg="Red")
    campos_para_digitar.pack(pady=40)

    nome = tk.Label(campos_para_digitar,
      text="Nome:",
      font= ("", 20, "bold"), 
      bg= "Red")
    nome.pack(pady= 2)

    entrada_nome = tk.Entry(campos_para_digitar, font=("", 15), bd= 4, relief='sunken')
    entrada_nome.pack(pady= 15)

    endereço = tk.Label(campos_para_digitar, text="Endereço", font=("", 25, "bold"), bg="Red")
    endereço.pack(pady= 2)
    entrada_endereco = tk.Entry(campos_para_digitar, font=("", 15), bd= 4, relief='sunken')
    entrada_endereco.pack(pady=2)

    botoes = tk.Frame(cadastro, bg="Green", bd= 10, relief="sunken")
    botoes.pack()

    def salvar():
     
     global Cliques

     pessoa = entrada_nome.get()
     endereço = entrada_endereco.get()

     cliente = Pessoa(pessoa, endereço)
     Cliques += 1
     
     abrir_cardapio(cliente)
     contar_cliques(1, cadastro)

    botao_de_cadastro = tk.Button(botoes,
     text="Escolher Pizza",
     font=("", 20, "bold"),
     command= salvar,
     bd= 4,
     relief="sunken",
     bg="Red")
    botao_de_cadastro.pack(pady= 10)

