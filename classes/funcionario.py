# Desenvolva a classe de Funcionario aqui
from datetime import date, datetime
from posixpath import split

class Funcionario:
    funcao = "Funcionário"

    def __init__(self, nome: str, cpf: str, salario: int = 3000):
        self.nome = " ".join(nome.split()).title()  
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d-%m-%Y")

    def __str__(self):
        return f"{self.funcao}: {self.nome}"
        