from classes import Funcionario
from helpers import StringHandler
from datetime import datetime

class Gerente(Funcionario):
    funcao = "Gerente"
    def __init__(self, nome: str, cpf: str, salario: int = 8000):
        self.nome = StringHandler.title_case(nome)
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")
        self.funcionarios = []

    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario):
        if funcionario.funcao != "Gerente":
            funcionario_ja_existe = [func for func in self.funcionarios if func["cpf"] == funcionario.cpf]
            if funcionario_ja_existe or funcionario.empresa != self.empresa:
                return False
        
            self.funcionarios.append(funcionario.__dict__)
            return True

        return False


    def aumento_salarial(self, funcionario, empresa):
        funcionario_ja_existe = [func for func in self.funcionarios if func["cpf"] == funcionario.cpf]

        if funcionario_ja_existe:
            valor_do_aumento = funcionario.salario * 0.1
            
            funcionario.salario = funcionario.salario + int(valor_do_aumento) 
        
            if funcionario.salario > 8000:
                funcionario.funcao = "Gerente"
                return funcionario
            
            return funcionario

        return False
            


       
        


        
        

        