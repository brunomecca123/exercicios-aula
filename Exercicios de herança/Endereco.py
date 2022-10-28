from Imovel import Imovel


class Endereco(Imovel):

    def __init__(self, rua, numero, bairro, preco_a_vista, preco_a_prazo):
        super().__init__(rua, numero, bairro, preco_a_vista, preco_a_prazo)

