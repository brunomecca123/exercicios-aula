from Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome, matricula, idade, plano_conta):
        super().__init__(nome, matricula, idade)
        self._plano_conta = plano_conta