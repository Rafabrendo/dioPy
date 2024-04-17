from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #assim q eu depositar eu vou chamar o metodo detalhes
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()


    def detalhes(self):
        print(f'Agência: {self.agencia} '
        f'Conta: {self.conta} '
        f'Saldo: {self.saldo}')
    
    #Assim que se faz methodos abstratos
    @abstractmethod
    def sacar(self, valor): pass
        


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
        

class ContaCorrrente(Conta):
    #limite=100 é um valor padrão. Porém, se eu quiser mandar mais ou menos, eu posso passar isso como parametro na chamada
    def __init__(self, agencia, conta, saldo, limite=100) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        #nesse caso vai poder sacar negativo até -100
        if (self.saldo + self.limite) < valor:
            print(f'Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
         