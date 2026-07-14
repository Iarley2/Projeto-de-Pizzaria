import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Funções.Abrir_menu_de_sabores import criar_pizza
from Classes.pizza import calabresa, frango, queijo, portuguesa, margherita, napolitana
from Classes.Cliente import Pessoa
import Imagens

def abrir_cardapio(cliente):

    cardapio = tk.Toplevel()
    cardapio.title("Cardápio")
    cardapio.geometry("800x800")
    cardapio.minsize(400, 300)
    cardapio.configure(bg="Brown",  bd= 10, relief="sunken")

    # Canvas
    canvas = tk.Canvas(cardapio, bg="Brown", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # Barra de rolagem
    scrollbar = ttk.Scrollbar(cardapio, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame onde ficará todo o conteúdo
    conteudo = tk.Frame(canvas, bg="Brown")
    canvas.create_window((0, 0), window=conteudo, anchor="nw")

    # Atualiza a área rolável
    conteudo.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

    acoes = tk.Frame(conteudo, bg="Red")

   
    acoes = tk.Frame(cardapio, bg="Red")
     
    acoes.pack(pady= 20)

    inicio = tk.Frame(conteudo)
    inicio.pack()
    titulo = tk.Label(inicio,
     text="Cardápio",
     font=("", 30, "bold", "italic"),
     bg= "brown",
     bd= 8,
     relief= "sunken")
    titulo.pack()

    FrameCalabresa = tk.Frame(conteudo,
     bg="Red",
     width= 100,
     height= 100,
     bd= 8,
     relief= "sunken")
    FrameCalabresa.pack(fill= "x")

    FrameFrango = tk.Frame(conteudo,
     bg="Red",
     width= 100,
     height= 100,
     bd= 8,
     relief= "sunken")
    FrameFrango.pack(fill= "x")

    FramePortuguesa = tk.Frame(conteudo,
     bg="Red",
     width= 100,
     height= 100,
     bd= 8,
     relief= "sunken")
    FramePortuguesa.pack(fill= "x")

    FrameMargherita = tk.Frame(conteudo,
    bg="red",
    width= 100,
    height= 100,
    bd= 8,
    relief= "sunken")
    FrameMargherita.pack(fill= "x")

    FrameNapolitana = tk.Frame(conteudo,
    bg="red",
    width= 100,
    height= 100,
    bd= 8,
    relief= "sunken")
    FrameNapolitana.pack(fill= "x")


    #Radiobuttons
    imagem_calabresa = cardapio.imagem_calabresa = tk.PhotoImage(file="Imagens/Calabresa.png")
    cardapio.imagem_calabresa = cardapio.imagem_calabresa.subsample(3, 3)

    imagem_frango = cardapio.imagem_frango = tk.PhotoImage(file= "Imagens/Frango.png")
    cardapio.imagem_frango = cardapio.imagem_frango.subsample(3, 3)

    imagem_portuguesa = cardapio.imagem_portuguesa = tk.PhotoImage(file= "Imagens/Portuguesa.png")
    cardapio.imagem_portuguesa = cardapio.imagem_portuguesa.subsample(3, 3)

    imagem_margherita = cardapio.imagem_margherita = tk.PhotoImage(file= "Imagens/Margherita.png")
    cardapio.imagem_margherita = cardapio.imagem_margherita.subsample(3, 3)

    imagem_napolitana = cardapio.imagem_napolitana = tk.PhotoImage(file= "Imagens/Napolitana.png")
    cardapio.imagem_napolitana = cardapio.imagem_napolitana.subsample(3, 3)

    PizzaEscolhida = tk.StringVar(value="")
    tk.Radiobutton(FrameCalabresa,
     text=f"{calabresa.sabor}\n{calabresa.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_calabresa,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Calabresa").pack(padx= 200)
    
    
    tk.Radiobutton(FrameFrango,
     text=f"{frango.sabor}\n{frango.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_frango,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Frango").pack(padx= 200)
    
    tk.Radiobutton(FramePortuguesa,
     text=f"{portuguesa.sabor}\n{portuguesa.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_portuguesa,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Portuguesa").pack(padx= 200)
    
    tk.Radiobutton(FrameMargherita,
     text=f"{margherita.sabor}\n{margherita.valor_inicial}",
     variable=PizzaEscolhida,
     image=cardapio.imagem_margherita,
     compound= "right",
     font= ("", 20, "bold"),
     bg= "red",
     bd= 8, 
     relief= "sunken",
     value="Margherita").pack(padx= 200)
    
    


    
    #botão final
    acoes = tk.Frame(conteudo,
     bg= "Brown")
    acoes.pack(pady= 20)

    def finalizar_pedido():
     escolha = PizzaEscolhida.get()
     cliente.cadastrar(escolha)

     messagebox.showinfo(
        "Pedido registrado \n com sucesso!", 
        f"Cliente: {cliente.nome}\n"
        f"Endereço: {cliente.endereco}\n"
        f"Escolha: {escolha}"
     )
     cardapio.destroy()


    finalizar = tk.Button(acoes,
     text="Finalizar pedido",
     bg= "Red", 
     command = finalizar_pedido, 
     font= ("", 20, "bold"), 
     bd= 10, 
     relief= "sunken")
    finalizar.pack(pady= 20)
    







    

    