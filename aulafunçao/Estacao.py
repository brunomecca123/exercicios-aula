class Estacao:
    def __init__(self, num, nome, passageiros, trem):
        self._num = num
        self._nome = nome
        self._passageiros = passageiros
        self._trem = trem

    def get_num(self):
        return self._num

    def set_num(self, num):
        self._num = num

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_trem(self):
        return self._trem

    def set_trem(self, trem):
        self._trem = trem

    def print_passageiros(self):
        for passag in self._passageiros:
            passag.to_string()

    def chegada(self, passageiro):
        self._passageiros.append(passageiro)

    def chegadas(self, passageiros):
        self._passageiros.extend(passageiros)

    def saida(self, passageiro):
        self._passageiros.remove(passageiro)

    def saidas(self, passageiros):
        for passag in passageiros:
            self._passageiros.remove(passageiro)

    def up_trem(self, passageiro, trem):
        if self._trem:
            trem.pick(passageiro)
            self._passageiros.remove(passageiro)
        else:
            print('O trem não está nessa estação')

    def ups_trem(self, passageiros, trem):
        if self._trem:
            for passag in passageiros:
                trem.pick(passag)
                self._passageiros.remove(passag)
        else:
            print('O trem não está nessa estação')

    def down_trem(self, passageiro, trem):
        self._passageiros.append(passageiro)
        trem.drop(passageiro)

    def downs_trem(self, passageiros, trem):
        self._passageiros.extend(passageiros)
        trem.drops(passageiros)

    def to_string(self):
        print("\n ### Estacao: " + str(self._num) + ' - ' + self._nome)
        print("Trem: " + str(self._trem))

        print('Lista de passageiros: ')

        for passag in self._passageiros:
            passag.to_string()

