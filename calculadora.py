# -*- coding: utf-8 -*-

"""
Calculadora
Autor: Tayan Matheus
Função: soma, divisão, multiplicação e subtração.
"""


print("--------- Calculadora---------")

sair = False

while sair == False:

    num1 = input("Digite o primeiro número: ")
    num1 = int(num1)  # forcando um string a virar numero
    operador = input("Digite o operador (+,-,/,* ): ")
    num2 = input("Digite o segundo número: ")
    num2 = int(num2)  # numero em string virando inteiro

    # + soma

    if operador == "+":
        operacao = num1 + num2

    #  - subtracao

    if operador == "-":
        operacao = num1 - num2

    # / divisao

    if operador == "/":
        operacao = num1 / num2

    # + multiplicacao

    if operador == "*":
        operacao = num1 * num2

    print("resultado: " + operacao)

    teste = input("Deseja sair? (s/n)")
    if teste == "s":
        sair = True
