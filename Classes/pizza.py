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
 ["Calabresa", "Queijo", "Tomate", "Cebola", "Orégano", "Azeitona"],
 40.00,
 ["Bacon", "Batata Palha", "Ketchup", "Maionese", "Mostarda"])

frango = Pizza("Frango", ["Queijo", "Catupiri", "Tomate", "Cebola"],
 40.00, 
 ["Bacon", "Batata Palha", "Ketchup", "Maionese", "Mostarda"])

queijo = Pizza("Queijo", ["Queijo, Orégano"], 40.00, [])



