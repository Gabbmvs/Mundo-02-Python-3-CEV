from random import randint
Pedra = 1
Papel = 2
Tesoura = 3

escolha_pc = randint(1,3)
escolha_player = int(input('Escolha entre: \n1-Pedra\n2-Papel\n3-Tesoura\nResposta: '))

#PC : Pedra com papel
if escolha_pc == 1 and escolha_player == 3:
  print('computador venceu com pedra')
#PC: Papel com Pedra
elif escolha_pc == 2 and escolha_player == 1:
  print('computador venceu com papel')
#PC: Tesoura com papel
elif escolha_pc == 3 and escolha_player == 2:
   print('computador venceu com tesoura ')
#Player : Tesoura com papel
elif escolha_player == 3 and escolha_pc == 2:
    print("Player venceu com tesoura")
#Player : Papel com pedra
elif escolha_player == 2 and escolha_pc == 1:
  print('Player Venceu com papel')
#Pedra com tesoura
elif escolha_player ==  1 and escolha_pc == 3:
  print('Player Venceu com pedra')
#empate
elif escolha_player == escolha_pc:
  print('Empate')
#Erro de respostar
elif escolha_player > 3 or escolha_player < 1:
  print('ERRO. RESPONDA NOVAMENTE.')