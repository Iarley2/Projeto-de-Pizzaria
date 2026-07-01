import tkinter as tk
from tkinter import ttk

MenuDaPizzaria = None

def main():
    MenuDaPizzaria = tk.Tk()
    MenuDaPizzaria.title("Pizzaria Raio de Sabores")
    MenuDaPizzaria.geometry("800x600")

    inicio = ttk.Frame(MenuDaPizzaria, padding=30)
    inicio.pack(fill="x")

    cabecalho = tk.Label( #Criação do título do menu
        MenuDaPizzaria, 
        text="Pizzaria Raio de Sabores", 
        font=("", 40),
        bg= "Green"
    )
    cabecalho.pack()

    cadastrar_Cliente = tk.Button(MenuDaPizzaria,
     text="Cadastrar-se",
     bg= "red",
     pady= 10,
     font=("", 20)).pack()

    MenuDaPizzaria.mainloop()

if __name__ == "__main__":
   main()
