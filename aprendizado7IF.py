import random
gerar = random.randrange(0,9)
num = input("Digite um numero\n") 
print('O numero aleatorio {} seu numero é {}'.format(gerar,	num))

if num == gerar:
    print('Acertou!')
else:
    print('Errou o numero gerado!') 