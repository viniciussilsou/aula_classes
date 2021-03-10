class Endereco:
    rua: str
    numero: str
    complemento: str
    bairro: str
    cep: str

    def __init__(
        self,
        rua: str,
        numero: str,
        complemento: str,
        bairro: str,
        cep: str):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
