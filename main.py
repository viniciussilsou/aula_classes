from catalogo_pessoa import CatalogoPessoa
from catalogo_endereco import CatalogoEndereco



if __name__ == "__main__":
    catalogo_endereco = CatalogoEndereco()
    novo_endereco = catalogo_endereco.criarEndereço(rua="Avenida Serrana", numero="187", complemento="Casa 1",
                                                    bairro="Pq. Paulista", cep="07844250")
    catalogo_pessoa = CatalogoPessoa()
    nova_pessoa = catalogo_pessoa.criar_pessoa(nome="Vinicius", email="vinicius@gmail.com", endereco=novo_endereco)




    pass

