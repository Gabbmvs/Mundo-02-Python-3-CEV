maior = 0
menor = 0
for i in range(4):
  peso = float(input('Diga seu peso: '))
  if i == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print(f'O maior peso lido foi de {maior}kg ')
print(f'O menor peso lido foi de {menor}kg')