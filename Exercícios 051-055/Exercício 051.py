primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo+(10 - 1) * razao

for pa in range(primeiro_termo, decimo + razao,razao):
  print(pa, end=' ➞ ')
print('fim')