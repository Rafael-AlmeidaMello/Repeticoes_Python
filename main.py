## Exercício 1

#for i in range(1,11):
#    print(i)

## Exercício 2

#for i in range(0,21,2):
#    print(i)

## Exercício 3

#numero = 0;

#for i in range(1,101):
#    numero = numero + i

#print(numero)

## Exercício 4

#total = 0

#for i in range(1,6):
#    nota = float(input("Digite sua nota: "))
#    total += nota

#media = total / 5
#print(f"A média é {media}")

## Exercício 5

#quantidade = int(input("quantos números você irá digitar? "))
#i = 0
#positivos = 0

#while i < quantidade:
#    numero = float(input("digite o número: "))
#    if numero > 0:
#        positivos = positivos + 1
#    i = i + 1

#print(positivos)

## Exercício 6

#tabuada = int(input("digite qual tabuada você deseja: "))

#for i in range(1, 11):
#    print(tabuada * i)

## Exercício 7

#numero = int(input("digite um número: "))
#fatorial = 1

#for i in range(numero, 1, -1):
#    fatorial *= i
    
#print("O resultado é ", fatorial)

## Exercício 8

#quantidade = int(input("Digite a quantidade de termos: "))

#a, b = 0, 1

#print("Sequência de Fibonacci:")

#for i in range(quantidade):
#    print(a, end=" ")
#    a, b = b, a + b

## Exercício 9

#senha = 123
#password = int(input("digite a senha: "))

#while password != senha:
#    password = int(input("senha incorreta, tente novamente: "))

#print("Login efetuado")

## Exercício 10

opcao = 0

while opcao != 4:
    print("MENU")
    print("1 - Olá")
    print("2 - Neymar")
    print("3 - Mostrar mensagem")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("Olá, usuário!")

        case 2:
            print("Neymar Júnior")

        case 3:
            print("Python é muito legal!")

        case 4:
            print("Você saiu")

        case _:
            print("Opção inválida!")