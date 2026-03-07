maiores = 0
menores = 0
for i in range(1,7,1):
  ano = int(input("Seu ano de nascimento: "))
  idade = 2025 - ano
  if idade >= 18:
    maiores += 1
  else:
   menores += 1
print(f'{maiores} pessoas são maiores de idade \n{menores} pessoas são menores de idade')