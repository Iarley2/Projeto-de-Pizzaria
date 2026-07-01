Cadastros = {}

class Cadastro:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
          Cadastros[self.nome] = self.endereco


