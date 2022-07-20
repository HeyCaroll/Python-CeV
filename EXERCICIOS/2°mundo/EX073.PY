from gettext import find


times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da  Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA','Avaí')
print('-=-'*30)
print(f'\033[;1mLista de times do Brasileirão:\033[;m {times}.')
print('-=-'*30)
print (f'\033[;1mOs 5 primeiros times são\033[;m {times[0:5]}.')
print('-=-'*30)
print (f'\033[;1mOs 4 últimos são\033[;m {times[-4:]}')
print('-=-'*30)
print(f'\033[;1mTimes em ordem alfabética:\033[;m {sorted(times)}')
print('-=-'*30)
print(f'\033[;1mO Chapecoense está na\033[;m {times.index("Chapecoence")+1}° posição')
print('-=-'*30)