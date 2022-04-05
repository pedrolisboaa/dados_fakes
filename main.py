from pessoa_fake import PessoaFake
from basededados import Dados

print(f'Bem vindo ao gerador de dados Fake!')
banco_de_dados = Dados()

# Inicio da aplicação
flag = True
while flag:

    resposta = int(input('O que deseja fazer: \n1 - Inserir dados \n2 - Visualizar todos dados \n3 - Deletar dados '
                         '\n4 - Alterar dados \n0 - Sair da aplicação \n'))
    if resposta == 0:
        flag = False
        continue

    if resposta == 1:
        qtd_pessoas = int(input('Informe quantas pessoas você gostaria de incluir em seu banco: '))
        for i in range(qtd_pessoas):
            pessoa = PessoaFake()
            dados_pessoa = pessoa.criar_nova_pessoa()
            banco_de_dados.inserir_dados(dados_pessoa)
        print(f'Dados inseridos com sucesso!')

    elif resposta == 2:
        pessoa = Dados()
        pessoa.mostrar_dados()
        print('TODOS DADOS VISUALIZADOS!')

    elif resposta == 3:
        id = int(input('Informe o ID que sera deletado: '))
        pessoa = Dados()
        pessoa.excluir_dados(id)

    else:
        id = int(input('Informe o ID que sera alterado: '))
        novo_telefone = input('Infome o novo telefone: ')
        #novo_email = input('Informe o novo e-mail: ')
        pessoa = Dados()
        pessoa.alterar_dados(id, novo_telefone)


# Encerrando conexão e programa
print(f'Até a próxima')
banco_de_dados.fechar_bd()
