from pessoa import Pessoa


class CatalogoPessoa:

    def criar_pessoa(self, nome: str, email: str, endereco: str) -> Pessoa:
        nova_pessoa = Pessoa(nome=nome, email=email, endereco=endereco)
        return nova_pessoa
