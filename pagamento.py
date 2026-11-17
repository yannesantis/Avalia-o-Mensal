class Pagamento:
    """Classe pai. As filhas sobrescrevem calcular_valor_final()."""
    nome = "Pagamento"

    def calcular_valor_final(self, valor: float) -> float:
        raise NotImplementedError("A classe filha deve implementar calcular_valor_final().")


class PagamentoDebito(Pagamento):
    nome = "Débito"

    def calcular_valor_final(self, valor: float) -> float:
        return valor  # sem acréscimo


class PagamentoPix(Pagamento):
    nome = "Pix"

    def calcular_valor_final(self, valor: float) -> float:
        return valor * 0.95  # desconto de 5%


class PagamentoDinheiro(Pagamento):
    nome = "Dinheiro"

    def calcular_valor_final(self, valor: float) -> float:
        return valor * 0.97  # desconto de 3%


class PagamentoCartao(Pagamento):
    nome = "Cartão"

    def calcular_valor_final(self, valor: float) -> float:
        return valor * 1.05  # acréscimo de 5%
