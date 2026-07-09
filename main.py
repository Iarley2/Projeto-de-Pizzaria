import tkinter as tk
from tkinter import ttk
from Funções.Abrir_cadastro import abrir_cadastro
from Funções.Abrir_menu_de_sabores import abrir_menu

def main():
    MenuDaPizzaria = tk.Tk()
    MenuDaPizzaria.title("Pizzaria Raio de Sabores")
    MenuDaPizzaria.geometry("800x800")
    MenuDaPizzaria.minsize(400, 300)
    MenuDaPizzaria.configure(bg= "Brown", bd= 10, relief= "sunken")

    inicio = tk.Frame(MenuDaPizzaria, bg="Brown", width= 100, height= 100)
    inicio.pack(pady= 20)

    cabecalho = tk.Label( #Criação do título do menu
        inicio,
        text="Pizzaria Raio de Sabores",
        font=("", 30, "bold", "italic"), 
        bd= 10, 
        relief= 'sunken'
    )
    cabecalho.pack()

    ações = tk.Frame(MenuDaPizzaria, bg="Brown", width= 100, height= 100, bd=10, relief="sunken")
    ações.pack(fill="x", pady= 80)

    cadastrar_Cliente = tk.Button(ações, #Botão de cadastrar
      text="Fazer meu pedido",
      font=("", 30, "bold"),
      command= abrir_cadastro,
      bd= 10,
      relief= "sunken",
      bg="red")
    cadastrar_Cliente.pack(pady=50)

    abrir_pizzas = tk.Button(ações,
     text= "Ver menu de sabores",
     font= ("", 30, "bold"), 
     command= abrir_menu,
     bd= 10,
     relief= "sunken",
     bg= "Green")
    abrir_pizzas.pack(pady=50)
    
    MenuDaPizzaria.mainloop()
        

if __name__ == "__main__":
   main()
