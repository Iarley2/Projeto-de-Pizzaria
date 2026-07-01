import tkinter as tk
from tkinter import ttk

MenuDaPizzaria = None

def main():
    MenuDaPizzaria = tk.Tk()
    MenuDaPizzaria.title("Pizzaria Raio de Sabores")
    MenuDaPizzaria.geometry("700x600")

    inicio = ttk.Frame(MenuDaPizzaria, padding=30)
    inicio.pack(fill="x")

    cabecalho = ttk.Label(
        MenuDaPizzaria, 
        text="Pizzaria Raio de Sabores", 
        font="Arial"
    )
    cabecalho.pack()

    MenuDaPizzaria.mainloop()

def abrir_cardapio():
    Cardapio = tk.Toplevel()
    Cardapio.title("Cardápio")
    Cardapio.minsize(480, 700)
  
    Cardapio.mainloop()

if __name__ == "__main__":
   main()
