import random

letras = "abcdefghijklmnopqrstuvxwyz"
numeros = "0123456789"
caracteres = "!@#$%¨&*()_+"

tamanho = 21
senha = ""

for i in range(tamanho):
    categoria = random.randint(1,3)

    if categoria == 1:
        letra_aleatoria = random.choice(letras)
        senha += letra_aleatoria
    elif categoria == 2:
        numero_aleatorio = random.choice(numeros)
        senha += numero_aleatorio
    else:
        caracter_aleatorio = random.choice(caracteres)
        senha += caracter_aleatorio

    print(f"A senha gerada foi: {senha}")