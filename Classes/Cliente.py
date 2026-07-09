class Pessoa:
     def __init__(self, pessoa, endereço):
        self.nome = pessoa
        self.endereco = endereço

     def cadastrar(self, escolha):
        with open("Pedidos.txt", "a") as pedido:
           pedido.write(f"\nNome: {self.nome} | Endereco: {self.endereco} | Escolha: {escolha}")