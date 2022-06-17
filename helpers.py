
class StringHandler:
    @classmethod
    def lower_case(self, string: str) -> str:
        '''Exemplo de retorno: "magazineluiza" '''
        return "".join(string.split()).lower()

    @classmethod
    def snake_case_lower(self, string: str) -> str:
        '''Exemplo de retorno: "jordan_cardoso_poole" '''
        return string.replace(" ", "_").lower()

    @classmethod
    def email_case(self, string1: str, string2: str) -> str:
        '''Recebe dois argumentos, o primeiro vai antes do "@". Exemplo de retorno: "jordan_cardoso_poole@magazineluiza.com" '''
        return f'{self.snake_case_lower(string1)}@{self.lower_case(string2)}.com'

    @classmethod
    def title_case(self, string: str) -> str:
        '''Exemplo de retorno: "Jordan Cardoso Poole" '''
        return " ".join(string.split()).title()


