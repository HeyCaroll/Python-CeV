import datetime
from time import sleep
print('\033[0;32mOlá, seja muito bem-vinda(o) ao formulario para alistamento militar!\033[m')
sleep (3)
print ('-=-'*20)
print ('''Para continuar, selecione o seu gênero
[ 1 ] Masculino
[ 2 ] Feminino
[ 3 ] Prefiro não dizer...''')
print ('-=-'*20)

x = int(input('Digite o número: '))
#caso o usario selecione masculino:
if x == 1:
    print('Vamos ao próximo passo!')
#caso o usario selecione feminino:
elif x == 2:
    print('O alistamento não é obrigatorio!')
    op = str(input('mesmo assim, tem interrese em se alistar?  '))
    if op in 'sim Sim SIM':
        print('Otimo, então vamos continuar')
    if op in 'Não não NÃO Nao nao NAO ':
        print ('ok, até mais!')
        exit()
#caso o usario não queria dizer seu genero:
elif x == 3:
    op = str(input('poxa, deseja continuar?'))
    if op in 'SIM Sim sim':
        print('Otimo, vamos continuar !')
    if op in 'NÃO NAO não nao':
        print('Ok, até mais!')
        exit()
#caso escolha uma opcão que não tenha
else:
    print ('\033[1;31mERRO!\033[m Opção invalida')
#alistamento de acordo com o ano de nascimento 
ano = int(input("Ano de nascimento? "))
hoje = int(datetime.datetime.now().year)
idade = hoje - ano
if idade < 18:
    print("Você não tem a idade ideal para se alistar no momento")
    print("Você ira se alistar em {}".format(ano +18))
elif idade == 18:
    print("já é a hora de se alistar!")
else:
    print("\033[1;31mJá passou do tempo para se alistar.\033[m")
    print("Você deveria ter se alistado em {}!".format(ano+18))
sleep (3)
print ("Fim do programa, volte sempre!")