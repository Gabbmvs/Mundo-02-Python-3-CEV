num = int(input("DIGA O NÚMERO: "))
tot = 0
for i in range (1, num+1):
  if num % i == 0:
    print('\033[34m', end=' ')
    tot += 1
  else:
    print('\033[33m', end= ' ')
  print(f'{i}', end= '')
print(f'\n\033[0mO Número {num} foi divisível {tot} vezes')
if tot  == 2:
  print('E por isso é primo')
else:
  print('Por isso ele não é primo')
