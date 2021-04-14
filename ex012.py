p = float(input('Digite o preço do produto: '))
d = p*(5/100)
print('O preço do produto é {} R$, o desconto é de {:.2f} R$'.format(p,d))
print('O valor do produto com desconto é de {:.2f} R$'.format(p-d))