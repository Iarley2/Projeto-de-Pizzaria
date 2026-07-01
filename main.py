import tkinter as tk
from tkinter import ttk

from Funções.Abrir_cadastro import abrir_cadastro

def main():
    MenuDaPizzaria = tk.Tk()
    MenuDaPizzaria.title("Pizzaria Raio de Sabores")
    MenuDaPizzaria.geometry("800x600")
    MenuDaPizzaria.minsize()

    inicio = ttk.Frame(MenuDaPizzaria, padding=30)
    inicio.pack(fill="x")

    cabecalho = ttk.Label( #Criação do título do menu
        inicio,
        text="Pizzaria Raio de Sabores",
        font=("", 30)
    )
    cabecalho.pack()

    ações = ttk.Frame(MenuDaPizzaria, padding=20)
    ações.pack(fill="x")

    cadastrar_Cliente = tk.Button(ações, #Botão de cadastrar
      text="Cadastrar-se",
      font=("", 30),
      command= abrir_cadastro).pack()
    
    abrir_cardápio = tk.Button(ações,
     text="Abrir cardápio \n (Se já posssui cadastro)",
     font=("", 30)).pack()

    MenuDaPizzaria.mainloop()
        

if __name__ == "__main__":
   main()
