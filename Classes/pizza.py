class Pizza:
    def __init__(self, sabor, ingredientes, valor_inicial, acompanhamentos):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.valor_inicial = valor_inicial
        self.acompanhamentos = acompanhamentos

    def mostrar_ingredientes(self):
        for i in self.ingredientes:
            return f"Ingredientes: {i}"
calabresa = Pizza("Calabresa",
 ["Calabresa", "Queijo", "Tomate"],
 40,
 ["Bacon", "Cogumelos"])

