l1 = float(input('Diga o l1: '))
l2 = float(input('Diga o l2: '))
l3 = float(input('Diga o l3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
  print('Isso é um triângulo!!\nAgora vamos descobrir se ele é um equilátero, isósceles ou escaleno')
  #condição com L1
  if l1 == l2 == l3:
    print('Esse Triângulo é equilátero')
  elif l1 == l2 != l3:
    print('Esse Triângulo é isósceles')
  elif l1 != l2 != l3:
    print('Esse Triângulo é escaleno')

#condição com L2
  elif l1 == l2 == l3:
    print('Esse Triângulo é equilátero')
  elif l3 == l2 != l1:
    print('Esse Triângulo é isósceles')
  elif l3 != l2 != l1:
    print('Esse Triângulo é escaleno')

#condição com L3
  elif l1 == l2 == l3:
    print('Esse Triângulo é equilátero')
  elif l3 == l1 != l2:
    print('Esse Triângulo é isósceles')
  elif l3 != l1 != l2:
    print('Esse Triângulo é escaleno')
else:
  print('Pelos lados, não pode ser um triângulo')