# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.
# while True
# num1 = int(input("digite um numero :  "))
# num2 = int(input("digite um numero :  "))
# soma = num1 + num2
# subtracao = num1 - num2
# divisao = num1 / num2
# mutipicacao = num1 * num2
# expoente = num1 ** num2

while True:
    
    num1 = int(input("digite um numero :  "))
    num2 = int(input("digite um numero :  "))

    print('''
            escolha a operaçao

    1 = soma          3 = divisao
    2 = subitraçao    4 = mutiplicaçao
            5 = elevado

    ''')
    menu = input("escolha a opraçao :")
    if menu == "1":
        soma = num1 + num2
        print(soma)
    elif menu == "2":
        subtracao = num1 - num2
        print(subtracao)
    elif menu == "3":
        divisao = num1 / num2
        print(divisao)
    elif menu == "4":
        mutipicacao = num1 * num2 
        print(mutipicacao)
    elif menu =="5":
        expoente = num1 ** num2
        print(expoente)
    elif menu =="6":  
        print("fim de p")  
        break
