import sqlite3
from datetime import datetime

print("Bem-vindo ao Mercadinho Mercosul!")

def inicializar_banco():
    conexao = sqlite3.connect('mercadinho.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            marca TEXT NOT NULL,
            validade_lote TEXT NOT NULL,
            setor TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            data_atualizacao TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

inicializar_banco()

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
    
    try:
        conexao = sqlite3.connect('mercadinho.db')
        cursor = conexao.cursor()
        data_agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor.execute('''
            INSERT INTO produtos (nome, preco, quantidade, marca, validade_lote, setor, data_criacao, data_atualizacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, preco, quantidade, marca, validade_lote, setor, data_agora, data_agora))
        conexao.commit()
        conexao.close()
        print("Produto registrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Produto com este nome já existe no banco de dados!")
    except Exception as e:
        print(f"Erro ao salvar produto: {e}")
   
def listar_produtos():
    try:
        conexao = sqlite3.connect('mercadinho.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        conexao.close()
        
        if not produtos:
            print("Nenhum produto registrado.")
        else:
            print("=== Produtos Registrados ===")
            for produto in produtos:
                id, nome, preco, quantidade, marca, validade_lote, setor, data_criacao, data_atualizacao = produto
                print(f"ID: {id} | Nome: {nome} | Preço: R${preco:.2f} | Quantidade: {quantidade} | Marca: {marca} | Validade/Lote: {validade_lote} | Setor: {setor}")
            print("===========================")
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")

def procurar_produto():
    nome = input("Digite o nome do produto que deseja procurar: ")
    marca = input("Digite a marca do produto que deseja procurar: ")
    try:
        conexao = sqlite3.connect('mercadinho.db')
        cursor = conexao.cursor()
        if marca:
            cursor.execute('SELECT * FROM produtos WHERE LOWER(nome) = LOWER(?) AND LOWER(marca) = LOWER(?)', (nome, marca))
        else:
            cursor.execute('SELECT * FROM produtos WHERE LOWER(nome) = LOWER(?)', (nome,))
        produto = cursor.fetchone()
        conexao.close()
        
        if produto:
            id, nome, preco, quantidade, marca, validade_lote, setor, data_criacao, data_atualizacao = produto
            print(f"Produto encontrado:")
            print(f"ID: {id} | Nome: {nome} | Preço: R${preco:.2f} | Quantidade: {quantidade} | Marca: {marca} | Validade/Lote: {validade_lote} | Setor: {setor}")
            print(f"Criado em: {data_criacao} | Atualizado em: {data_atualizacao}\n")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao procurar produto: {e}")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    marca = input("Digite a marca do produto que deseja remover: ")
    try:
        conexao = sqlite3.connect('mercadinho.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT id FROM produtos WHERE LOWER(nome) = LOWER(?) AND LOWER(marca) = LOWER(?)', (nome, marca))
        produto = cursor.fetchone()
        
        if produto:
            id = produto[0]
            cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
            conexao.commit()
            conexao.close()
            print("Produto removido com sucesso!")
        else:
            conexao.close()
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao remover produto: {e}")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    marca = input("Digite a marca do produto que deseja atualizar: ")
    try:
        conexao = sqlite3.connect('mercadinho.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT id FROM produtos WHERE LOWER(nome) = LOWER(?) AND LOWER(marca) = LOWER(?)', (nome, marca))
        produto = cursor.fetchone()
        
        if produto:
            id = produto[0]
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
            
            data_agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute('''
                UPDATE produtos 
                SET preco = ?, quantidade = ?, marca = ?, validade_lote = ?, setor = ?, data_atualizacao = ?
                WHERE id = ?
            ''', (novo_preco, nova_quantidade, nova_marca, nova_validade_lote, novo_setor, data_agora, id))
            conexao.commit()
            conexao.close()
            print("Produto atualizado com sucesso!")
        else:
            conexao.close()
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Registrar produto")
        print("2 - Listar produtos")
        print("3 - Procurar produto")
        print("4 - Remover produto")
        print("5 - Atualizar produto")
        print("0 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            registrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            procurar_produto()
        elif opcao == '4':
            remover_produto()
        elif opcao == '5':
            atualizar_produto()
        elif opcao == '0':
            print("Obrigado por usar o Mercadinho Mercosul! Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
