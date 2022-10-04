from Trem import Trem
from Estacao import Estacao
from Passageiro import Passageiro

def print_estado(trem, estacoes):
    trem.to_string()

    for

if __name__ == "__main__":
trem = Trem([], 10)

    pass1 = Passageiro('Fernando', 27)
    pass2 = Passageiro('Vinicius', 30)
    pass3 = Passageiro('jao', 35)
    pass4 = Passageiro('eu', 10)
    pass5 = Passageiro('voce', 50)
    pass6 = Passageiro('nos', 42)
    pass7 = Passageiro('vos', 24)
    pass8 = Passageiro('eles', 21)
    pass9 = Passageiro('tu', 15)
    pass10 = Passageiro('alala', 70)
    pass11 = Passageiro('dasdskad', 95)

    estacao_a = Estacao(1, 'A', [], True)
    estacao_b = Estacao(2, 'B', [], False)
    estacao_c = Estacao(3, 'C', [], False)

    estacao_a.chegadas([pass1, pass2, pass3, pass4])
    estacao_b.chegadas([pass5, pass6, pass7, pass8])
    estacao_c.chegadas([pass9, pass10, pass11])

    estacoes = []
    estacoes.extend([estacao_a, estacao_b, estacao_c])

    estacao_a.ups_trem([pass1, pass2, pass3], trem)
    