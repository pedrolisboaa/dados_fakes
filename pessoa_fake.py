from faker import Faker
from gerador_de_cpf import generate_cpf


class PessoaFake():
    def __init__(self):
        self.fake = Faker(['pt_BR'])
        self.nome = self.fake.name()
        self.cpf = generate_cpf()
        self.nascimento = self.fake.date()
        self.telefone = self.fake.phone_number()
        self.email = self.fake.ascii_company_email()

    def criar_nova_pessoa(self):
        return self.nome, self.cpf, self.nascimento, self.telefone, self.email,


if __name__ == '__main__':
    teste = PessoaFake()
    dado_teste = teste.mostrar_dados()
    print(dado_teste)


