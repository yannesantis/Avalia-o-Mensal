from datetime import datetime
from produto import Produto
from item_venda import ItemVenda

class Venda:
    def __init__(self):
        self.data = datetime.now()
        self.valor_total = 0.0
        self.itens = []  # Lista para guardar os itens

    def calcular_total(self) -> float:
        """Percorre todos os itens e soma os subtotais."""
        self.valor_total = sum(item.calcular_subtotal() for item in self.itens)
        return self.valor_total

    def adicionar_item(self, produto: Produto, quant: int):
        """Verifica o estoque, cria o ItemVenda e adiciona à lista."""
        if produto.decrementar_estoque(quant):
            novo_item = ItemVenda(quant, produto)
            self.itens.append(novo_item)
            print(f"Item adicionado: {quant}x {produto.descricao}")
            self.calcular_total()
        else:
            print(f"Erro: Estoque insuficiente para {produto.descricao} (Disponível: {produto.estoque})")

    def remover_item(self, produto: Produto):
        """Busca o item pelo produto, remove e devolve ao estoque."""
        item_para_remover = None
        for item in self.itens:
            if item.produto == produto:
                item_para_remover = item
                break
        
        if item_para_remover:
            # Devolve a quantidade ao estoque do produto
            produto.estoque += item_para_remover.quantidade
            self.itens.remove(item_para_remover)
            print(f"Item removido: {produto.descricao}")
            self.calcular_total()
        else:
            print(f"Item {produto.descricao} não encontrado na venda.")
