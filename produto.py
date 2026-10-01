class Produto:
    def __init__(self, descricao: str, preco_unitario: float, estoque: int):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def decrementar_estoque(self, quant: int) -> bool:
        """Diminui o estoque se houver quantidade suficiente."""
        if self.estoque >= quant:
            self.estoque -= quant
            return True
        return False

    def __str__(self):
        return f"{self.descricao} (R$ {self.preco_unitario:.2f})"
