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

    titulo = ttk.Frame(cadastro, padding= 20)
    titulo.pack()

    texto = ttk.Label(titulo,
     text="Pedido", font= ("", 20, "bold", "italic")).pack()
    
    campos_para_digitar = ttk.Frame(cadastro, padding=20)
    campos_para_digitar.pack()

    nome = ttk.Label(campos_para_digitar, text="Nome:", font=("", 25))
    nome.pack()
    entrada_nome = tk.Entry(campos_para_digitar, font=("", 15))
    entrada_nome.pack()

    endereço = ttk.Label(campos_para_digitar, text="Endereço", font=("", 25))
    endereço.pack()
    entrada_endereco = tk.Entry(campos_para_digitar, font=("", 15))
    entrada_endereco.pack()

    botoes = ttk.Frame(cadastro, padding= 20)
    botoes.pack()

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
     bg="red")
    botao_de_cadastro.pack()

