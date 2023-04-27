alfabeto = "abcdefghijklmnopqrstuvwxyz"
chave = "qwertyuiopasdfghjklzxcvbnm"

mensagem = input("Digite aqui a palavra ou senha a ser criptografada: ").lower()

mensagem_criptografada = ""

for letra in mensagem:
    if letra in alfabeto:
        indice = alfabeto.index(letra)
        nova_letra = chave[indice]
        mensagem_criptografada += nova_letra
    else:
        mensagem_criptografada += letra

print(f"A senha ficou assim: {mensagem_criptografada}")