resposta = int(input('Diga qual será a base de conversão de números.\n----------------------------------------------\n1-Para binário\n2-Para octal\n3-Para hexadecimal\nResposta: '))
if resposta == 1:
  print('Você escolheu Binário!')
  num1 = int(input('Diga o número: '))
  print(f'O número convertido em binário é {bin(num1)[2:]}') # o [2:] SERVE PARA APARECER APENAS O NÚMERO E TIRAR O 0b ou 0o ou 0h
elif resposta == 2:
  print('Você escolheu Octal!')
  num2 = int(input('Diga o número: '))
  print(f'O número convertido em octal é  {oct(num2)[2:]}')
elif resposta == 3:
  print('Você escolheu Hexadecimal!')
  num3 = int(input('Diga o número: '))
  print(f'O número convertido em hexadecimal é: {hex(num3)[2:]}')
elif resposta > 3 or resposta < 1:
  print('Resposta inválida...')