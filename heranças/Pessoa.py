class Pessoa:
    def __init__(self, nome, matricula, idade):
        self._nome = nome
        self._matricula = matricula
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade