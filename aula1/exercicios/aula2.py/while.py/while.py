# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string
aluno = str (input("escreva seu nome "))
qdd_nota = int(input())
nota1 = float(input("digite suya nota "))
nota2 = float(input("digite suya nota "))
nota3 = float(input("digite suya nota "))
nota4 = float(input("digite suya nota "))
media =(nota1 + nota2 + nota3 +nota4 )/4
print(f"sua media e {media}")