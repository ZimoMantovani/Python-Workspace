class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo_ = False
        
    def __str__(self):
        return f'Nome do titular: {self.titular} \n Saldo: {self.saldo}'        
    
    def ativar_conta(self):
        if not self.ativo_:
            self.ativo_ = True
            print('Usuario ativo')
    
    
    
    
    
    
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)
print(conta1)
ContaBancaria.ativar_conta(conta1)


conta3 = ContaBancaria("Fernanda", 1500)
print(f'Valor propriedade titular: {conta3.saldo}')


# class ContaBancariaPythonica:
#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False
        
#     @property
#     def __str__(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo
    
    
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
        
        
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta
        
    
    
    
    
cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

cliente4 = ClienteBanco.criar_conta("Cleito",1000)
print(cliente4)