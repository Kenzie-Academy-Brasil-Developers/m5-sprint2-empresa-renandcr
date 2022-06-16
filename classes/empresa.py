import os
import json
from datetime import datetime

class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.nome = " ".join(nome.split()).title()
        self.cnpj = cnpj
        self.contratados = []

    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self, funcionario):
        newFuncionario = funcionario.__dict__

        email = f"{newFuncionario['nome'].strip().replace(' ', '_').lower()}@{self.nome.replace(' ', '').lower()}.com"
        empresa = self.nome

        newFuncionario["email"] = email
        newFuncionario["empresa"] = empresa

        isHired = False
        for x in self.contratados:
            if x["cpf"] == newFuncionario["cpf"]:
                isHired = True
                return "Funcionário com esse CPF já foi contratado."
    
        if not isHired:
            self.contratados.append(newFuncionario)
            return "Funcionário contratado!"

    def gerar_holerite(self, funcionario):
        isHired = False
        for x in self.contratados:
            if x["cpf"] == funcionario.__dict__["cpf"]:
                isHired = True

                if not os.path.exists(f"./empresas/{self.nome.replace(' ', '_').lower()}"):
                    os.makedirs(f"./empresas/{self.nome.replace(' ', '_').lower()}")
   
                funcionarioHolerite = funcionario.__dict__.copy()

                del funcionarioHolerite["email"]
                del funcionarioHolerite["empresa"]

                funcionarioHolerite["mes"] = datetime.now().strftime("%B") 

                with open(f"./empresas/{self.nome.replace(' ', '_').lower()}/{funcionarioHolerite['nome'].replace(' ', '_').lower()}.json", "w") as write_file:
                    json.dump(funcionarioHolerite, write_file, indent=2)

                return True
            
        if not isHired:
            return False

    @staticmethod
    def ler_holerite(empresa, funcionario):
        pathEmpresa = empresa.__dict__["nome"].replace(" ", "_").lower()
        pathFuncionario = funcionario.__dict__["nome"].replace(" ", "_").lower()
        paySlipExists = os.path.exists(f"./empresas/{pathEmpresa}/{pathFuncionario}.json")

        if paySlipExists:
            with open(f"./empresas/{pathEmpresa}/{pathFuncionario}.json", "r") as file_funcionario:
                return json.load(file_funcionario)

        else:
            return "Holerite não gerado!"


    def demissao(self, funcionario):
        if len(self.contratados) == 0:
            return "Não há funcionários contratados nesta empresa"

        elif funcionario.funcao == "Gerente":
            for x in self.contratados:
                if x["cpf"] == funcionario.cpf:
                    self.contratados.remove(x)
                    return "Gerente demitido!"
        
        for func_current in self.contratados:
            if func_current["cpf"] == funcionario.cpf:
                            self.contratados.remove(func_current)
        
        if funcionario.funcao == "Funcionário":
            for func_current in self.contratados:
                for key_funcionarios, value in func_current.items():
                    if key_funcionarios == "funcionarios":  
                        for current in value:
                            if current["cpf"] == funcionario.cpf:
                                value.remove(current)
                                return "Funcionário demitido"
        
        return "Não consta esse CPF na empresa"
                
            

    def promocao(self, funcionario):
        if funcionario.funcao == "Funcionário":
            for func in self.contratados:
                if func["cpf"] == funcionario.cpf:
                    funcionario.funcao = "Gerente"
                    return funcionario

        return False


