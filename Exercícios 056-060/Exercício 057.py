resposta = input('diga seu sexo [M/F]? ').upper()[0]
while resposta not in 'MmFf':
  resposta = input('Dados inválidos diga seu sexo [M/F]? ').upper()[0]
print(f'Sexo {resposta} registrado')
