from banco import Banco
from cliente import Cliente
from conta import ContaCorrrente, ContaPoupanca


banco = Banco()

cliente1 = Cliente('Rafa', 24)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_clientes(cliente2)

banco.inserir_conta(conta1)
banco.inserir_conta(conta2)

banco.inserir_clientes(cliente3)


#condição para autenticação no banco.
if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20) 

else:
    print('Cliente não autenticado.')

print('###' * 30)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(99) 

else:
    print('Cliente não autenticado.')