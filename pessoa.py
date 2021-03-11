

class Pessoa:
    nome: str
    email: str
    endereco: str

    def __init__(
        self,
        nome: str,
        email: str,
        endereco: str
    ):
        self.nome = nome
        self.email = email
        self.endereco = endereco
