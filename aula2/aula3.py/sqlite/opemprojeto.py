arquivo = open(r"C:\Users\67795\Documents\aula python\aulapython_wenderson\aula2\aula3.py\sqlite\pesquisa.csv","r")

#arquivo = open(r"endereço","r")
#r =read = leitura
# a = appende =adiciona
# w = write = escreve por cima
for pessoa in arquivo:
    pessoa = pessoa.replace('","','";"')  #troca virgula por ponto e virtgula
    pessoa= pessoa.replace('"','')
    print(pessoa.split(";")) #transformas em lista