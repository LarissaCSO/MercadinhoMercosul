print("Bem-vindo ao Mercadinho Mercosul!")

produtos = []

def registrar_produto():
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço inválido. Por favor, insira um número.")
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            break
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro.")
    marca = input("Digite a marca do produto: ")
    validade_lote = input("Digite a validade/lote do produto: ")
    setor = input("Digite o setor do produto: ")
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "marca": marca,
        "validade_lote": validade_lote,
        "setor": setor
    }   
    produtos.append(produto)
    print("Produto registrado com sucesso!")
   
def listar_produtos():
    if not produtos:
        print("Nenhum produto registrado.")
    else:
        print("Produtos registrados:")
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Marca: {produto['marca']}, Validade/Lote: {produto['validade_lote']}, Setor: {produto['setor']}")

def procurar_produto():
    nome = input("Digite o nome do produto que deseja procurar: ")
    marca = input("Digite a marca do produto que deseja procurar: ")
    encontrado = False
    for produto in produtos:
        if produto['nome'].lower() == nome.lower() and produto['marca'].lower() == marca.lower():
            print(f"Produto encontrado: Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Marca: {produto['marca']}, Validade/Lote: {produto['validade_lote']}, Setor: {produto['setor']}")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    marca = input("Digite a marca do produto que deseja remover: ")
    for produto in produtos:
        if produto['nome'].lower() == nome.lower() and produto['marca'].lower() == marca.lower():
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    marca = input("Digite a marca do produto que deseja atualizar: ")
    for produto in produtos:
        if produto['nome'].lower() == nome.lower() and produto['marca'].lower() == marca.lower():
            while True:
                try:
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    break
                except ValueError:
                    print("Preço inválido. Por favor, insira um número.")
            while True:
                try:
                    nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                    break
                except ValueError:
                    print("Quantidade inválida. Por favor, insira um número inteiro.")
            nova_marca = input("Digite a nova marca do produto: ")
            nova_validade_lote = input("Digite a nova validade/lote do produto: ")
            novo_setor = input("Digite o novo setor do produto: ")
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            produto['marca'] = nova_marca
            produto['validade_lote'] = nova_validade_lote
            produto['setor'] = novo_setor
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def menu():
    while True:
        print("Menu:")
        print("1. Registrar produto")
        print("2. Listar produtos")
        print("3. Procurar produto")
        print("4. Remover produto")
        print("5. Atualizar produto")
        print("6. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            registrar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            procurar_produto()
        elif escolha == '4':
            remover_produto()
        elif escolha == '5':
            atualizar_produto()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()
