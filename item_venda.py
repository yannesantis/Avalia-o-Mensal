from produto import Produto

class ItemVenda:
    def __init__(self, quantidade: int, produto: Produto):
        self.quantidade = quantidade
        self.produto = produto
        # O valor do item é calculado automaticamente
        self.valor_item = quantidade * produto.preco_unitario

    def calcular_subtotal(self) -> float:
        return self.valor_item

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao} - Subtotal: R$ {self.valor_item:.2f}"
