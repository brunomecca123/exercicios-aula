from Funcionario import Funcionario


class Gerente(Funcionario):

    def __init__(self, nome, matricula, idade, salario, departamento):
        super().__init__(nome, matricula, idade, salario)
        self._departamento = departamento

    def get_bonificacao(self):
        return 0.2 * self._salario