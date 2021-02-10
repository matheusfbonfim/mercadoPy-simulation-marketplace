from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

# Lista de produtos
produtos: List[Produto] = []

# Uma lista de dicionarios
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('======================================')
    print('=========== Bem-vindo(a) =============')
    print('=========== Matheus Shop =============')
    print('======================================')

    print('\nSelecione uma das opções abaixo:')
    print('\t1 - Cadastrar produto')
    print('\t2 - Listar produtos')
    print('\t3 - Comprar produtos')
    print('\t4 - Visualizar carrinho')
    print('\t5 - Fechar pedido')
    print('\t6 - Sair do sistema')

    opcao: int = int(input('Opção: '))

    # Opções redirecionando para as funções
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('===================')

    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input("Informe o preco do produto: "))

    # Instancia de produto
    produto: Produto = Produto(nome, preco)

    # Adicionando a lista de produtos
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)

    # Volta para o menu
    menu()


def listar_produtos() -> None:
    # Listar somente se tiver produtos
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')

        for produto in produtos:
            print(produto)
            print('---------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados')

    # Volta para o menu
    sleep(2)
    menu()


def comprar_produto() -> None:
    # Verifica se existe produtos na lista
    if len(produtos) > 0:
        print("Informe o código do produto que deseja adicionar ao carrinho: ")
        print('--------------------------------------------------------------')
        # Mostrar código de produtos
        print("================= Produtos Disponíveis =======================")

        for produto in produtos:
            print(produto) # print reescrito com o __str__ -> class Produto
            print('----------------------------------------------------------')
            sleep(1)

        codigo: int = int(input("\nCódigo: "))

        produto: Produto = pega_produto_por_codigo(codigo)

        # Verifica se o produto existe na lista de produtos
        if produto:
            # Verifica se o produto já está no carrinho
            if len(carrinho) > 0:
                # Verifica se o produto ja esta no carrinho e só incrementa a quantidade
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto) # Valor em um dicionario (chave:valor)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant+1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                # Produto ainda nao esta no carrinho
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f"O produto com código {codigo} não foi encontrado")
            sleep(2)
            menu()

    else:
        print("Ainda não existem produtos para vender")

    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho: ")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------------')
                sleep(1)

    else:
        print("Ainda não existem produtos no carrinho")

    sleep(2)
    menu()


def fechar_pedido() -> None:
    # Fechar pedido se o carrinho tiver algo
    if len(carrinho) > 0:
        # Somatório do valor total
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():  # Items -> Chave:Valor
                print(dados[0])  # Posição 0 -> Chave -> Produto
                print(f'Quantidade: {dados[1]}')  # Posicao 1 -> Quantidade
                valor_total += dados[0].preco * dados[1]
                print('---------------')
                sleep(1)

        # Mostra o valor da fatura
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')

        # Despede
        print('Volte sempre!')

        # Limpa o carrinho
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')

    # Executa o menu novamente
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    # Retorna o produto
    return p


if __name__ == '__main__':
    main()
