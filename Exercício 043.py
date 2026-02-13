altura = float(input('Me dê sua altura em M:'))
peso = float(input('Me dê seu peso em Kg: '))
imc = float(peso / (altura * altura))

if imc > 18.5 and imc < 25:
  print('peso ideal')
elif imc > 25 and imc < 30:
  print('sobrepeso')
elif imc  > 30 and imc < 40:
  print('obesidade')
elif imc > 40:
  print('obesidade mórbida')
else:
  print('abaixo do peso ideal')
