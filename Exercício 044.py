valor = float(input('Valor desse produto R$: R$'))
opcao = int(input('Qual a forma de pagamento?\n1-Dinheiro/Cheque\n2-À vista no cartão\n3-Parcelado\nResposta: '))

if opcao == 1:
  print(f'Você tem 10% de desconto, agora o valor do produto está R${valor - (valor * 0.1)}')
elif opcao == 2:
  print(f'Você tem 5% de desconto, agora o valor do produto está em R${valor - (valor * 0.05)}')
elif opcao == 3:
  parcelado = int(input('Em quantas vezes?\n1- 2 vezes\n2- 3 vezes\nResposta: '))
  if parcelado == 1:
    print(f'A parcela fica R${valor/2} ')
  elif parcelado == 2:
    juros = valor * 0.20 * 3
    print(f'A parcela fica R${valor + juros}, com R${juros/3} de juros cada mês')
else:
  print('Opção inválida...')