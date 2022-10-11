class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def to_string(self):
        print('Cliente: ' + self._nome + '\nidade: ' + str(self._idade))