from datetime import datetime
import json
import os
from helpers import StringHandler
class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.nome = StringHandler.title_case(nome)
        self.cnpj = cnpj
        self.contratados = []

    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self, funcionario) -> None | str:
        funcionario.email = StringHandler.email_case(funcionario.nome, self.nome)
        funcionario.empresa = self.nome
        funcionario_ja_existe = [func for func in self.contratados if func["cpf"] == funcionario.cpf]

        if funcionario_ja_existe:
            return "Funcionário com esse CPF já foi contratado"

        self.contratados.append(funcionario.__dict__)
        return "Funcionário contratado!"

    def gerar_holerite(self, funcionario):
        funcionario_copia = funcionario.__dict__.copy()
        caminho_diretorio_empresa = f"empresas/{StringHandler.snake_case_lower(self.nome)}"
        funcionario_ja_existe = [func for func in self.contratados if func["cpf"] == funcionario.cpf]

        if not funcionario_ja_existe:
            return False

        if not os.path.exists(caminho_diretorio_empresa):
            os.makedirs(caminho_diretorio_empresa)

        funcionario_copia["mes"] = datetime.now().strftime("%B")
        del funcionario_copia["email"]
        del funcionario_copia["empresa"]

        with open(f"{caminho_diretorio_empresa}/{StringHandler.snake_case_lower(funcionario.nome)}.json", "w") as arquivo:
            json.dump(funcionario_copia, arquivo, indent=2)
            return True

    @staticmethod
    def ler_holerite(empresa, funcionario):
        caminho_holerite_ja_existe = f"empresas/{StringHandler.snake_case_lower(funcionario.empresa)}/{StringHandler.snake_case_lower(funcionario.nome)}.json"

        if not os.path.exists(caminho_holerite_ja_existe):
            return "Holerite não gerado"

        with open(caminho_holerite_ja_existe, "r") as arquivo_encontrado:
            arquivo_funcionario = json.load(arquivo_encontrado)
            return arquivo_funcionario

    
    def demissao(self, funcionario):
        funcionario_ja_existe = [func for func in self.contratados if func["cpf"] == funcionario.cpf]

        if funcionario_ja_existe:
            if funcionario.funcao == "Gerente":
                for func in self.contratados:
                    if func["cpf"] == funcionario.cpf:
                        self.contratados.remove(func)
                        return "Gerente demitido!"
            
            elif funcionario.funcao == "Funcionário":
                for func in self.contratados:
                    if func["cpf"] == funcionario.cpf:
                        self.contratados.remove(func)

                for func in self.contratados:
                    try:
                        if func["funcionarios"]:
                            for x in func["funcionarios"]:
                                if x["cpf"] == funcionario.cpf:
                                    func["funcionarios"].remove(x)
                                    return "Funcionário demitido!"
                    except:
                        pass

        return "Não consta esse CPF na empresa"
                        

    def promocao(self, funcionario):
        if funcionario.funcao == "Funcionário":
            funcionario_ja_existe = [func for func in self.contratados if func["cpf"] == funcionario.cpf]

            if funcionario_ja_existe:
                funcionario.funcao = "Gerente"
                return funcionario

        return False

    



            


        



    

