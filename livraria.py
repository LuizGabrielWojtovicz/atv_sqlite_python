import sqlite3

# -------------------------------------------------------------------------------------------- #

def adicionar_livro(nome_livro, nome_autor, ano_lancamento, valor):

    db = sqlite3.connect('livraria.db')
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    ''', (nome_livro, nome_autor, ano_lancamento, valor))
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def exibir_livros():

    db = sqlite3.connect('livraria.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM livros')
    lista_livros = cursor.fetchall()

    for item in lista_livros:
        print(f"Id -> {item[0]} | Título -> {item[1]} | Autor -> {item[2]} | Ano -> {item[3]} | Preço: {item[4]}")
    db.close()

# -------------------------------------------------------------------------------------------- #

def atualizar_valor_livro(nome_livro, novo_valor):

    db = sqlite3.connect('livraria.db')
    cursor = db.cursor()
    cursor.execute('''
        UPDATE livros 
          SET preco = ? 
        WHERE titulo = ?
    ''', (novo_valor, nome_livro))
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def remover_livro_por_titulo(nome_livro):

    db = sqlite3.connect('livraria.db')
    cursor = db.cursor()
    cursor.execute('''
        DELETE FROM livros 
         WHERE titulo = ?
    ''', (nome_livro,))
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def buscar_livros_por_autor(nome_autor):

    db = sqlite3.connect('livraria.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT titulo 
          FROM livros 
         WHERE autor = ?
    ''', (nome_autor,))
    livros_encontrados = cursor.fetchall()
    if livros_encontrados:
        print(f"Livros do autor {nome_autor}:")
        for livro in livros_encontrados:
            print(f"- {livro[0]}")
    else:
        print(f"Nenhum livro encontrado para o autor {nome_autor}.")
    
    db.close()

# -------------------------------------------------------------------------------------------- #

db = sqlite3.connect('livraria.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        preco REAL NOT NULL
    )
''')
db.commit()
db.close()

while True:
    opcao_escolhida = input('''\n1. Adicionar novo livro
                               \n2. Exibir todos os livros
                               \n3. Atualizar preço de um livro
                               \n4. Remover um livro
                               \n5. Buscar livros por autor
                               \n6. Sair
                               \n\nEscolha uma opção:\n''')

    if opcao_escolhida == '1':

        titulo_livro = input("Título: ")
        autor_livro = input("Autor: ")
        ano_publicacao = int(input("Ano de publicação: "))
        preco_livro = float(input("Preço: "))
        adicionar_livro(titulo_livro, autor_livro, ano_publicacao, preco_livro)

    elif opcao_escolhida == '2':

        exibir_livros()

    elif opcao_escolhida == '3':

        titulo_livro = input("Título do livro para atualizar o preço: ")
        novo_preco_livro = float(input("Novo preço: "))
        atualizar_valor_livro(titulo_livro, novo_preco_livro)

    elif opcao_escolhida == '4':

        titulo_livro = input("Título do livro para remover: ")
        remover_livro_por_titulo(titulo_livro)

    elif opcao_escolhida == '5':

        nome_autor = input("Digite o nome do autor: ")
        buscar_livros_por_autor(nome_autor)

    elif opcao_escolhida == '6':
        print("Saiu | :)")
        break

    else:
        print("Opção não existente.")
