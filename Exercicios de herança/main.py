from Endereco import Endereco
from Imovel import Imovel

if __name__ == '__main__':

    imovel1 = Imovel('Ruaaa', 723, 'Centro', 1000, 1000)
    print('-----PRIMEIRO IMOVEL------')
    print(imovel1.get_rua())
    print(imovel1.get_numero())
    print(imovel1.get_bairro())
    print(imovel1.get_precoV())
    print(imovel1.get_precoP())


