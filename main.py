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
        font=("Arial", 50),
        bg= "Green"
    )
    cabecalho.pack()

    acoes = tk.Button(MenuDaPizzaria, text="Fazer Pedido", command=abrir_cardapio,
    pady=60,
    padx=80,
    fg="White", bg="Red").pack()

    MenuDaPizzaria.mainloop()

def abrir_cardapio():
    Cardapio = tk.Toplevel()
    Cardapio.title("Cardápio")
    Cardapio.minsize(480, 700)
  
    Cardapio.mainloop()

if __name__ == "__main__":
   main()
