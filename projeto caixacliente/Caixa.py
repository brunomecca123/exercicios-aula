import time
class Caixa:
    def __init__(self, num, aberto, fila_clientes):
        self._num = num
        self._aberto = aberto
        self._fila_clientes = fila_clientes

    def atende_cliente(self):
        if self._aberto:
            cliente = self._fila_clientes.pop(0)
            print("Cliente sendo atendido...")
            time.sleep(1)

            print("Atendimento do cliente " + cliente.get_nome())
            return cliente

        print("Caixa fechado")

    def enfileira_cliente(self, cliente):
        self._fila_clientes.append(cliente)

    def to_string(self):
        print("\nCaixa: " + str(self._num))
        print("Clientes: ")
        for cliente in self._fila_clientes:
            cliente.to_string()

