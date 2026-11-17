from produto import Produto
from venda import Venda
from pagamento import PagamentoDebito, PagamentoPix, PagamentoDinheiro, PagamentoCartao

mouse = Produto("Mouse sem fio", 49.90, 100)
camisa = Produto("Camisa Polo", 50.00, 100)

pagamentos = [PagamentoDebito(), PagamentoPix(), PagamentoDinheiro(), PagamentoCartao()]

for pagamento in pagamentos:
    venda = Venda(pagamento)
    venda.adicionar_item(mouse, 2)
    venda.adicionar_item(camisa, 1)
    print(venda)
