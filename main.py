from produto import Produto
from venda import Venda

def main():
    print("--- Iniciando Sistema de Vendas (Python) ---\n")

    p1 = Produto("Camiseta", 50.00, 10)
    p2 = Produto("Calça Jeans", 120.00, 5)
    p3 = Produto("Tênis", 200.00, 2)

    venda1 = Venda()
    print(f"Data da Venda: {venda1.data.strftime('%d/%m/%Y %H:%M:%S')}\n")

    venda1.adicionar_item(p1, 2) # 2 Camisetas (100)
    venda1.adicionar_item(p2, 1) # 1 Calça (120)
    
    print("\nTentando comprar 3 tênis (só temos 2):")
    venda1.adicionar_item(p3, 3) 

    print(f"\nValor Total da Venda: R$ {venda1.calcular_total():.2f}")

    # 5. Remover um item
    print("\n--- Removendo Item ---")
    venda1.remover_item(p1) # Remove a camiseta

    # 6. Mostrar Total Atualizado e Estoque
    print(f"\nNovo Valor Total: R$ {venda1.calcular_total():.2f}")
    print(f"Estoque atual de {p1.descricao}: {p1.estoque} unidades (voltou ao estoque)")

if __name__ == "__main__":
    main()
