sal = float(input('Digite o salario do funcionário: '))
au10 = (sal * 10 / 100)
au15 = (sal * 15 / 100)
if sal >= 1250:
    print('O salario é de {} R$, o aumento é de {} R$, então o salario passou a ser de {} R$'.format(sal, au10, sal + au10))
else:
    print('O salario é de {} R$, o aumento é de {} R$, então o salario passou a ser de {} R$'.format(sal, au15, sal + au15))