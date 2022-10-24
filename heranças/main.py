from Pessoa import Pessoa
from Funcionario import Funcionario
from Cliente import Cliente
from Gerente import Gerente



if __name__ == '__main__':

    pessoa1 = Pessoa('augusto', 1, 72)
    print(pessoa1.get_nome())

    pessoa2 = Cliente('ana', 2, 24, 'Ouro')
    print(pessoa2.get_nome())

    pessoa3 = Gerente('Gerente: ' 'JOSE', 3, 32, 100000, 'rh')
    print(pessoa3.get_nome() + ' Salario: ' + str(pessoa3.get_bonificacao()))

    pessoa4 = Funcionario('BIXAO FUNCIONARIO', 4, 56, 100000)
    print(pessoa4.get_nome() + ': ' + str(pessoa4.get_bonificacao()))
