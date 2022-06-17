from datetime import datetime
from helpers import StringHandler

class Funcionario:
    funcao = "Funcionário"
    def __init__(self, nome: str, cpf: str, salario: int = 3000):
        self.nome = StringHandler.title_case(nome)
        self.cpf = cpf
        self.salario = salario 
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.funcao}: {self.nome}"

    