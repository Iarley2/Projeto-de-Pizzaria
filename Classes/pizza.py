class Pizza:
    def __init__(self, sabor, ingredientes, valor_inicial, acompanhamentos):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.valor_inicial = valor_inicial
        self.acompanhamentos = acompanhamentos

calabresa = Pizza("Calabresa", ["Calabresa", "Queijo", "Tomate"], 40, ["Bacon", "Cogumelos"])