# valor da casa, salário e quantos anos  a prestação não pode ser mais de 30% do salário
# Divido o valor da casa pela quantidade de anos, que vai dar o valor da parcela
# e a prestação não pode ser maior que 30% do salário da pessoa

valor_casa = float(input('Qual o valor da casa em R$? : R$'))
salario = float(input('Qual o seu salário em R$? : R$'))
anos = int(input('Em quantos anos você pretende pagar??'))

parcela = valor_casa/(anos*12)

if parcela > salario*0.3:
  print(f'Não podemos realizar o empréstimo, a parcela no valor {parcela:.2f} é maior que 30% do seu salário')
else:
    emprestimo = float(input('Pode realizar o empréstimo...\nQuanto deseja? R$'))
    print('Empréstimo realizado!')
