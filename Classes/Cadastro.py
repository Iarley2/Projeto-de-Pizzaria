Cadastros = {}

class Cadastro:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = int(senha)

    def cadastrar(self):
        if len(Cadastros) < 6:
          Cadastros[self.nome] = self.senha


