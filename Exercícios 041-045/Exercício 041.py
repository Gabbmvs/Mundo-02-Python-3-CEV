ano_idade = int(input('Que ano você nasceu? '))
ano_atual = int(input('Que ano estamos? '))
idade = ano_atual - ano_idade
if idade <= 9 :
  print('mirim')
elif idade <= 14 :
  print('infantil')
elif idade <= 19 :
  print('júnior')
elif idade <= 25 :
  print('sênior')
elif idade > 25 :
 print('Master')
