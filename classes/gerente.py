# Desenvolva a classe de Gerente aqui
from classes.empresa import Empresa
from classes import Funcionario
class Gerente(Funcionario):
    funcao = "Gerente"

    def __init__(self, nome, cpf, salario = 8000):
        super().__init__(nome, cpf, salario)
        self.funcionarios = []
    
    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario):
        if funcionario.funcao != "Funcionário" or funcionario.empresa != self.empresa:
            return False
        elif len(self.funcionarios) == 0:
            self.funcionarios.append(funcionario.__dict__)
            return True
        else:
            for x in self.funcionarios:
                if x["cpf"] == funcionario.cpf:
                    return False

        self.funcionarios.append(funcionario.__dict__)
        return True


    def aumento_salarial(self, funcionario, empresa):
        funcionarioAtual = [func for func in self.funcionarios if func["cpf"] == funcionario.cpf]

        if not funcionarioAtual:
            return False

        else:
            valorDoAumento = funcionarioAtual[0]["salario"] * 0.1
            funcionarioAtual[0]["salario"] = int(funcionarioAtual[0]["salario"] + valorDoAumento)
            if funcionarioAtual[0]["salario"] > 8000:
                funcionario.funcao = "Gerente"
                return funcionario
            
            return funcionario




       
        


        
        

        