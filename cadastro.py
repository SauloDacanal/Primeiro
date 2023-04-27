from time import sleep

print(40*"=")
print("Olá, bem vindo ao meu projeto!!")
print(40*"=")

nome = input("Digite seu nome: ")
print(f"{nome}, A calculadora esta iniciando: ")
sleep(3)

print(f"{nome}, A calculadora foi iniciada!! ")

continua = "s"
while(continua == "s"):
    num1 = float(input("Digite o primeiro númro: "))
    op = input("Digite um operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if(op == "+"):
        resultado = num1 + num2
    elif(op == "-"):
        resultado = num1 - num2
    elif(op == "*"):
        resultado = num1 * num2
    elif(op == "/"):
        resultado = num1 / num2
    else:
        resultado = 0

    print(f"resultado: {resultado}")

    continua = input("Deseja continuar? (s/n): ")