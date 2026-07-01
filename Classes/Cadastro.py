Cadastros = {}

class Cadastro:
    def __init__(self, nome, senha, endereco):
        self.nome = nome
        self.senha = int(senha)
        self.endereco = endereco

    def cadastrar(self):
        if len(Cadastros) < 6:
          Cadastros[self.nome] = self.senha


