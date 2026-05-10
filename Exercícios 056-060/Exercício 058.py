from random import randint
numero = randint(0, 10)
tentativas = 0
resposta = int(input('Jogo de adivinhação: \nDiga o número que pensei até acertar! '))
if resposta == numero:
  print(f'VOCÊ ACERTOU!\nQuantidade de tentativas : {tentativas}')
while resposta != numero:
  resposta = int(input('Tente novamente: '))
  tentativas += 1
print(f'VOCÊ ACERTOU!\nQuantidade de tentativas : {tentativas}')