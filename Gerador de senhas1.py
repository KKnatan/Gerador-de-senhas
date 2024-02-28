import random
from time import sleep

print('-'*43)
print('Seja Muito bem vindo ao gerador de senhas!')
print('-'*43)


caract='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*[/?'
resp=''
while True:
    quanti = int(input("Quantas senhas você quer gerar?"))
    # quantidade de senhas a se gerar
    compri = int(input("Quantos caracteres a senha deve ter?"))
    # Comprimento da senha
    for c in range(quanti): # vai gerar o tanto de senhas a ser gerado
        senhas=''
        for g in range(compri): # aqui é o range da quantidade de caracteres
            senhas+=random.choice(caract) #randomiza os caracteres com base na quantidade do comprimento
        print(f'{senhas}')
        sleep(.6)
    resp = str(input('Deseja gerar mais senhas? [S/N]')).strip().upper()
    if resp in 'S':
        sleep(.6)
    if resp in 'N':
        break
print('>>Programa Encerrado<<')