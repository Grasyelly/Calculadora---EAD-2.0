import os
from time import sleep
num1 = 0
num2 = 0
op = ''
result = 0

#Ferramenta utilizada para deixar a calculadora em looping:
while True:
    #Inserção do primeiro número
    num1 = int(input("           Calculadora\n================================\n Informe o primeiro número: "))
    
    #Escolha da operação
    op = input("\n            Operações\n================================\n        (+) Adição\n        (-) Subtração\n        (*) Multiplicação\n        (/) Divisão\n        (&) Potenciação\n        (#) Radiciação\n\n Informe a operação desejada: ")
    
    #Estrutura para identificar se o usuário tenha escolhido a opção "(#) Raiz"
    if op == '#':
        result = num1 ** 0.5
        print('\n           Resultado\n================================\n          √' + str(result))
        sleep(2)
        os.system('clear') or None
    else:
        #Estrutura utilizada para a escolha das demais operações
        num2 = int(input("\n================================\n  Informe o segundo número: "))
        
        #Adição
        if op == '+':
            result = num1 + num2
        #Subtração
        elif op == '-':
            result = num1 - num2
        #Multiplicação
        elif op == '*':
            result = num1 * num2
        #Divisão
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Operação inválida'
        #Potenciação
        elif op == '&':
            result = num1 ** num2
        print('\n           Resultado\n================================\n          ' + str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(result))
        sleep(2)
        os.system('clear') or None