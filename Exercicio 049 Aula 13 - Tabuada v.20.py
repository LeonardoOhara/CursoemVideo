#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('digite para ver uma tabuada'))
for t in range (1 , 11):
    print(f'{n} x {t} = {t*n}')


