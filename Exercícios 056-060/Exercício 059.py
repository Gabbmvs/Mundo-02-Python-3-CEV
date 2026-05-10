n1 = int(input('Diga um número: '))
n2 = int(input('Diga um número: '))

while resposta <= 5 and resposta > 0:
  resposta = int(input('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa\nDiga o que você deseja fazer com os números: '''))
  if resposta == 1:
    print(n1 + n2)

  elif resposta == 2:
     print(n1 * n2)
  if resposta == 3:
    if n1 > n2:
          print(n1)
    else:
          print(n2)

  elif resposta == 4:
     n1 = int(input('Diga um número: '))
     n2 = int(input('Diga um número: '))

  elif resposta == 5:
     print('Terminando programa!')
     break


