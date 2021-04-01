from datetime import date
ano = int(input('Que ano quero analisar? Coloque 0 para analisar a data atual: '))
if ano == 0:
    ano = date.today().year # modulo para informar apenas o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # se o ano for divisivel por 4 e o resto for 0 entao ele é bissexto # se o ano for divisivel por 100 e o resto for diferente de 0 # se o ano for divisivel por 400 e o resto for igual a 0
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))
