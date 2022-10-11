
from Pilha import Pilha

if __name__ == '__main__':


    pilha = Pilha()
    ob1 = {
        'nome': 'dsadasd',
        'turma': 32
    }
    ob2 = {
        'nome': 'aaaaaaaa',
        'turma': 55
    }
    ob4 = {
        'nome': 'bbbbbbbbbb',
        'turma': 60
    }



    pilha.empilha(ob1)
    pilha.empilha(ob2)
    pilha.empilha(ob4)
    ob3 =  pilha.desempilha()
    print(pilha.first())

    

    pilha.to_string()

