# Avalia-o-Mensal
Explicação de como foi feito:

o que foi feito:
Implementei o sistema em Python utilizando os conceitos de Orientação a Objetos (Classes, Atributos, Métodos, Associação e Encapsulamento). Criei a lógica de negócio para que o sistema não permita vender produtos sem estoque e devolva a quantidade ao estoque caso um item seja removido da venda.

Organização do Projeto:
Criei a pasta sisvenda contendo os seguintes arquivos:

produto.py: Classe Produto (com o método decrementar_estoque).

item_venda.py: Classe ItemVenda (com o cálculo de subtotal).

venda.py: Classe Venda (com a lista de itens e métodos de adicionar, remover e calcular total).

main.py: Arquivo de teste que simula uma venda real, incluindo tentativa de compra sem estoque e remoção de item.

Como testar:
Basta executar o arquivo main.py no terminal (comando: python main.py) para ver o sistema funcionando.
