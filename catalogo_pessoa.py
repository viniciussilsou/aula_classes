from pessoa import Pessoa


class CatalogoPessoa:

    def criar_pessoa(self, nome: str, email: str) -> Pessoa:
        nova_pessoa = Pessoa(nome=nome, email=email)
        return nova_pessoa
