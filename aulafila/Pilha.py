class Pilha:

    def __init__(self):
        self._itens = []

    def esta_vazia(self):
        return self._itens == []

    def empilha(self, item):
       return self._itens.append(item)

    def desempilha(self):
        return self._itens.pop()

    def first(self):
        return self._itens[len(self._itens) - 1]

    def get_tamanho(self):
        return len(self._itens)

    def to_string(self):
        print("Quantidade de elementos: " + str(self.get_tamanho()))

        for item in self._itens:
            print(item)