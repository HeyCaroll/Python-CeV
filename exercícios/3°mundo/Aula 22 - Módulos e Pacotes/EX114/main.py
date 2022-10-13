import urllib.error
import urllib.request

try:
    global site
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\nO site pudim não está acessível no momento.')
else:
    print('\nConsegui acessar o site pudim com sucesso.')
