import tkinter as tk
from tkinter import ttk
from Classes.Cliente import Cadastros, Cadastro


def abrir_cadastro():
    cadastro = tk.Toplevel()
    cadastro.title("Cadastro")
    cadastro.geometry("800x600")
    cadastro.minsize(400, 300)

    titulo = ttk.Frame(cadastro, padding= 20)
    titulo.pack()

    texto = ttk.Label(titulo,
     text="Cadastro", font= ("", 20)).pack()
    
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

    def salvar():
     pessoa = entrada_nome.get()
     endereco = entrada_endereco.get()

     cliente = Cadastro(pessoa, endereco)
     cliente.cadastrar()

     print(Cadastros)

     abrir_cardápio = tk.Button(ações,
     text="Abrir cardápio",
     font=("", 15)).pack()


    ações = ttk.Frame(cadastro, padding=20)
    ações.pack()

    botão_de_cadastro = tk.Button(ações, text="Cadastrar", command= salvar, pady= 15)
    botão_de_cadastro.pack()

