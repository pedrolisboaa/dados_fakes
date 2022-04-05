import sqlite3


class Dados:
    def __init__(self):
        self.conexao = sqlite3.connect('dados_fakes.db')
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, dado):
        self.cursor.execute('INSERT INTO clientes (nome, cpf, nascimento, telefone, email) VALUES (?, ?, ?, ?, ?)', dado)
        self.conexao.commit()
        print()

    def mostrar_dados(self):
        contador = 0
        self.cursor.execute('SELECT * FROM clientes')
        for linha in self.cursor.fetchall():
            contador += 1
            print(linha)

        print(f'Sua tabela possui {contador} dados')
        print()

    def excluir_dados(self, id):
        sql = ('DELETE FROM clientes WHERE id=?')
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        print('DADO DELETADO')
        print()

    def alterar_dados(self, id, telefone):
        self.cursor.execute('UPDATE clientes SET telefone=:telefone WHERE id=:id', {'telefone': telefone, 'id': id})
        self.conexao.commit()
        print('DADO ALTERADO')
        print()

    def fechar_bd(self):
        self.cursor.close()
        self.conexao.close()



