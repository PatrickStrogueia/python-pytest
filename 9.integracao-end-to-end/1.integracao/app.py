class Produto:
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self,produto):
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade

    def verifica_quantidade(self,nome_produto):
        return self.produtos.get(nome_produto,0)
    
"""
No terminal:
python
from app import Produto, Estoque
produto1 = Produto("Mouse",10)
print(produto1.nome)
print(produto1.quantidade)
estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(Produto("Teclado",5))
print(estoque.verifica_quantidade("Mouse"))
print(estoque.verifica_quantidade("Teclado"))
quit()
"""