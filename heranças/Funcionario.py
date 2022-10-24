from Pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome, matricula, idade, salario):
        super().__init__(nome, matricula, idade)
        self._salario = salario

    def get_bonificacao(self):
        return 0.15 * self._salario