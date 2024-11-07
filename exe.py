produtos = [] 
categorias = set()  

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")

    produto = (nome, preco, categoria)
    produtos.append(produto)

    categorias.add(categoria)

def exibir_produtos():
    if produtos:
        print("\nProdutos cadastrados:")
        for nome, preco, categoria in produtos:
            print(f"Nome: {nome}, Preço: {preco}, Categoria: {categoria}")
    else:
        print("\nNenhum produto cadastrado ainda.")

def exibir_categorias():
    if categorias:
        print("\nCategorias cadastradas:")
        for categoria in categorias:
            print(categoria)
    else:
        print("\nNenhuma categoria cadastrada.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Cadastrar um novo produto")
        print("2 - Ver as categorias sem duplicatas")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            exibir_categorias()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
