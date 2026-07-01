import tkinter as tk
from tkinter import ttk
from Classes import Cadastro

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

    nome = ttk.Label(campos_para_digitar, text="Nome:")
    nome.pack()
    entrada_nome = tk.Entry(campos_para_digitar)
    entrada_nome.pack()

    def salvar():
        cliente = Cadastro(entrada_nome.get())


    ações = ttk.Frame(cadastro, padding=20)
    ações.pack()

    botão_de_cadastro = tk.Button(ações, text="Cadastrar", command= salvar).pack()

