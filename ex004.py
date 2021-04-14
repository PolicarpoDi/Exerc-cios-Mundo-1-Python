n1 = input('Digite algo: ')
print('o tipo primitivo desse valor é ', type(n1))
print('É um tipo letra ou numero? ',n1.isalnum())
print('É maiusculo? ',n1.isupper())
print('É uma letra? ',n1.isalpha())
print('É um decimal? ', n1.isdecimal())
print('é numerico? ', n1.isnumeric())
print('É um espaço?{}'.format(n1.isspace()))


