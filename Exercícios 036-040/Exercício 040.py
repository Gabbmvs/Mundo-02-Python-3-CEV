ano_atual = int(input('Que ano estamos? '))
ano_nascimento = int(input('Ano que você nasceu: '))
idade = ano_atual - ano_nascimento
if idade > 18:
  print('Já passou do tempo do alistamento')
elif idade < 18:
  print('Se safou do exército')
else:
  print('Vamos se alistar no exército parceiro')