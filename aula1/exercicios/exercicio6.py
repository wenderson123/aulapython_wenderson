# Crie um programa que solicite ao cliente
# o nome do produto
# o preço do produto
# a quantidade
# e mostre usando o f-string
nome_produto =input("nome do produto ")
preco =float(input("preço do produto "))
quantidade = int(input("quantidade "))

print(f"nome do produto:{nome_produto} preco do produto:{preco} quantidade: {quantidade:.2f}")
#:.2f significa 2 casa depois do ponto e op f significa float