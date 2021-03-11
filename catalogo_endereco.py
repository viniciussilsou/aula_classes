from endereco import Endereco

class CatalogoEndereco:

    def criarEndereço (self,
        rua: str,
        numero: str,
        complemento: str,
        bairro: str,
        cep: str) -> Endereco:

        novo_endereco = Endereco(rua=rua, numero=numero, complemento=complemento,bairro=bairro,cep=cep)

        return novo_endereco