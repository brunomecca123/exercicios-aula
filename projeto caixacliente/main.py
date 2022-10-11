from Cliente import Cliente
from Caixa import Caixa



if __name__ == '__main__':
    c1 = Cliente('Bruno ', + 15)
    c2 = Cliente('Joao ', + 20)
    c3 = Cliente('Mateus ', + 55)

    caixa1 = Caixa(1, True, [])
    caixa2 = Caixa(2, True, [])


    caixa1.enfileira_cliente(c1)
    caixa1.enfileira_cliente(c2)
    caixa2.enfileira_cliente(c3)

    caixa1.atende_cliente()
    caixa1.to_string()
    caixa2.to_string()




