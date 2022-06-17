from urllib import request, error

try:
    site = request.urlopen('https://www.cursoemvideo.com')

except error.URLError:
    print('O site pudim não está acessível no momento. Tente novamente mais tarde!')

else:
    print('O site pudim está acessível!')
    print(site.read())
