import tkinter as tk
from tkinter import ttk

from Funções.Abrir_cardapio import abrir_cardapio, escolha
from Funções.cliques import contar_cliques

Cliques = 0

def abrir_cadastro():

    cadastro = tk.Toplevel()
    cadastro.title("Pedido")
    cadastro.geometry("800x600")
    cadastro.minsize(400, 300)
    cadastro.configure(bg="Brown")

    titulo = tk.Frame(cadastro, bd= 4, relief="sunken", bg="Brown")
    titulo.pack(pady= 20)

    texto = ttk.Label(titulo,
     text="Pedido", font= ("", 20, "bold", "italic")).pack()
    
    campos_para_digitar = tk.Frame(cadastro, bd= 10, relief="sunken", bg="Brown")
    campos_para_digitar.pack(pady=40)

    nome = tk.Label(campos_para_digitar,
      text="Nome:",
      font= ("", 20, "bold"), 
      bg= "Brown")
    nome.pack(pady= 2)

    entrada_nome = tk.Entry(campos_para_digitar, font=("", 15), bd= 4, relief='sunken')
    entrada_nome.pack(pady= 15)

    endereço = tk.Label(campos_para_digitar, text="Endereço", font=("", 25, "bold"), bg="Brown")
    endereço.pack(pady= 2)
    entrada_endereco = tk.Entry(campos_para_digitar, font=("", 15), bd= 4, relief='sunken')
    entrada_endereco.pack(pady=2)

    botoes = tk.Frame(cadastro, bg="Brown")
    botoes.pack()

    class Pessoa:
     def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

     def cadastrar(self):
        with open("Pedidos.txt", "a") as pedido:
           pedido.write(f"\nNome: {self.nome} | Endereço: {self.endereco} | Escolha: ")
 

    def salvar():
     
     global Cliques

     pessoa = entrada_nome.get()
     endereco = entrada_endereco.get()

     cliente = Pessoa(pessoa, endereco)
     cliente.cadastrar()
     Cliques += 1
     
     abrir_cardapio()
     contar_cliques(1, cadastro)

    botao_de_cadastro = tk.Button(botoes,
     text="Escolher Pizza",
     font=("", 20, "bold"),
     command= salvar,
     bd= 4,
     relief="sunken",
     bg="Red")
    botao_de_cadastro.pack(pady= 10)

