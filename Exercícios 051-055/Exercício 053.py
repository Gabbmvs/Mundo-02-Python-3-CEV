frase = input("Digite uma frase: ")

# Remove espaços e coloca tudo em minúsculo
frase_tratada = frase.replace(" ", "").lower()

# Inverte manualmente usando laço
invertida = ""

for letra in frase_tratada:
    invertida = letra + invertida

# Verificação
if frase_tratada == invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")