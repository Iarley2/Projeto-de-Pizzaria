import tkinter as tk
from tkinter import ttk

MenuDaPizzaria = None

def main():
    MenuDaPizzaria = tk.Tk()
    MenuDaPizzaria.title("Pizzaria Raio de Sabores")
    MenuDaPizzaria.geometry("600x700")
    MenuDaPizzaria.minsize(480, 700)

    conteudo = ttk.Frame(MenuDaPizzaria)
    conteudo.pack(fill="both", expand=True)

    ttk.Button(conteudo, text="Fazer pedido", command=abrir_cardapio).pack()

    MenuDaPizzaria.mainloop()

    

def abrir_cardapio():
    Cardapio = tk.Toplevel()
    Cardapio.title("Cardápio")
    Cardapio.minsize(480, 700)
  
    Cardapio.mainloop()

if __name__ == "__main__":
   main()
