import abc


class Imovel(abc.ABC):


    def __init__(self, rua, numero, bairro, preco_a_vista, preco_a_prazo):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._preco_a_vista = preco_a_vista
        self._preco_a_prazo = preco_a_prazo

    def get_rua(self):
        return self._rua

    def get_numero(self):
        return self._numero

    def get_bairro(self):
        return self._bairro

    def get_precoV(self):
        return 1 * self._preco_a_vista

    def get_precoP(self):
        return 1.5 * self._preco_a_prazo
