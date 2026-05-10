somaidade = 0
media_idade = 0
totmulher20 = 0
for p in range(1, 4):
  print(f'----{p}° PESSOA----')
  nome = input('Nome: ').strip()
  idade = int(input('Idade: '))
  sexo = input('Sexo [M/F]: ')
  somaidade += idade
  if p == 1 and sexo in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = idade
  if sexo in 'Ff' and idade < 20:
    totmulher20 += 1
media_idade = somaidade / 4
print(f'O nome do homem mais velho é {nomevelho} com {maioridadehomem} anos')
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')