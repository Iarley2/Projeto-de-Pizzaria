import tkinter as tk
from tkinter import ttk
from Funções.Abrir_cadastro import abrir_cadastro
from Funções.Abrir_menu_de_sabores import abrir_menu

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
        font=("", 30, "bold")
    )
    cabecalho.pack()

    ações = ttk.Frame(MenuDaPizzaria, padding=20)
    ações.pack(fill="x")

    cadastrar_Cliente = tk.Button(ações, #Botão de cadastrar
      text="Fazer meu pedido",
      font=("", 30, "bold"),
      command= abrir_cadastro,
      bg="red")
    cadastrar_Cliente.pack()

    abrir_pizzas = tk.Button(ações,
     text= "Ver menu de sabores",
     font= ("", 30, "bold"), 
     command= abrir_menu,
     bg= "Green")
    abrir_pizzas.pack()
    
    MenuDaPizzaria.mainloop()
        

if __name__ == "__main__":
   main()
