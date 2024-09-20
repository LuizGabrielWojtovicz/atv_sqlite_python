import sqlite3

# -------------------------------------------------------------------------------------------- #

def adicionar_funcionario(nome_func, cargo_func, salario_func, depto_func):

    db = sqlite3.connect('empresa.db')
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO funcionarios (nome, cargo, salario, departamento)
        VALUES (?, ?, ?, ?)
    ''', (nome_func, cargo_func, salario_func, depto_func))
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def exibir_funcionarios():

    db = sqlite3.connect('empresa.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * 
                        FROM funcionarios''')
    lista_funcionarios = cursor.fetchall()
    if lista_funcionarios:
        for func in lista_funcionarios:
            print(f"Id -> {func[0]} | Nome -> {func[1]} | Cargo -> {func[2]} | Salário -> {func[3]} | Departamento -> {func[4]}")
    else:
        print("Nenhum funcionário cadastrado.")
    db.close()

# -------------------------------------------------------------------------------------------- #

def atualizar_salario_funcionario(nome_func, novo_salario):

    db = sqlite3.connect('empresa.db')
    cursor = db.cursor()
    cursor.execute('''
        UPDATE funcionarios SET salario = ? WHERE nome = ?
    ''', (novo_salario, nome_func))
    if cursor.rowcount == 0:
        print(f"Funcionário {nome_func} não encontrado.")
    else:
        print(f"Salário de {nome_func} atualizado para {novo_salario}.")
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def remover_funcionario(nome_func):

    db = sqlite3.connect('empresa.db')
    cursor = db.cursor()
    cursor.execute('''
        DELETE FROM funcionarios 
         WHERE nome = ?
    ''', (nome_func,))
    if cursor.rowcount == 0:
        print(f"Funcionário {nome_func} não encontrado.")
    else:
        print(f"Funcionário {nome_func} removido com sucesso.")
    db.commit()
    db.close()

# -------------------------------------------------------------------------------------------- #

def buscar_funcionarios_por_depto(depto_func):

    db = sqlite3.connect('empresa.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT * 
          FROM funcionarios 
         WHERE departamento = ?
    ''', (depto_func,))
    lista_funcionarios = cursor.fetchall()
    if lista_funcionarios:
        print(f"Funcionários do departamento {depto_func}:")
        for func in lista_funcionarios:
            print(f"- {func[1]} | Cargo -> {func[2]} | Salário -> {func[3]}")
    else:
        print(f"Nenhum funcionário encontrado no departamento {depto_func}.")
    
    db.close()

# -------------------------------------------------------------------------------------------- #

db = sqlite3.connect('empresa.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL,
        departamento TEXT NOT NULL
    )
''')
db.commit()
db.close()

while True:
    
    opcao = input('''\nMenu de Opções:")
                     \n1. Adicionar novo funcionário")
                     \n2. Exibir todos os funcionários")
                     \n3. Atualizar salário de um funcionário")
                     \n4. Remover um funcionário")
                     \n5. Buscar funcionários por departamento
                     \n6. Sair
                     \n\nEscolha uma opção: \n''')

    if opcao == '1':

        nome_func = input("Nome: ")
        cargo_func = input("Cargo: ")
        salario_func = float(input("Salário: "))
        depto_func = input("Departamento: ")
        adicionar_funcionario(nome_func, cargo_func, salario_func, depto_func)

    elif opcao == '2':

        exibir_funcionarios()

    elif opcao == '3':

        nome_func = input("Nome do funcionário para atualizar o salário: ")
        novo_salario = float(input("Novo salário: "))
        atualizar_salario_funcionario(nome_func, novo_salario)

    elif opcao == '4':

        nome_func = input("Nome do funcionário para remover: ")
        remover_funcionario(nome_func)

    elif opcao == '5':

        depto_func = input("Digite o nome do departamento: ")
        buscar_funcionarios_por_depto(depto_func)

    elif opcao == '6':

        print("Saiu | :)")
        break

    else:
        print("Opção não existente.")

