import requests
import re

romantycznosc = requests.get('https://wolnelektury.pl/media/book/txt/ballady-i-romanse-romantycznosc.txt')
testament_moj = requests.get('https://wolnelektury.pl/media/book/txt/testament-moj.txt')
stepy_akremanskie = requests.get('https://wolnelektury.pl/media/book/txt/sonety-krymskie-stepy-akermanskie.txt')
bogurodzica = requests.get('https://wolnelektury.pl/media/book/txt/bogurodzica.txt')
cierpienie = requests.get('https://wolnelektury.pl/media/book/txt/baczynski-wiersz-o-cierpieniu.txt')

# podzial wierszy na slowa ( rozdzielenie przez spacje formanty tekstu oraz utworzenie listy slow )
slowa_romantycznosc = re.split(r'[\r\n\s\.\,\;\:]',romantycznosc.text)
slowa_testament_moj = re.split(r'[\r\n\s\.\,\;\:]',testament_moj.text)
slowa_stepy_akremanskie = re.split(r'[\r\n\s\.\,\;\:]',stepy_akremanskie.text)
slowa_bogurodzica = re.split(r'[\r\n\s\.\,\;\:]',cierpienie.text)
slowa_cierpeienie = re.split(r'[\r\n\s\.\,\;\:]',bogurodzica.text)

while ('' in slowa_romantycznosc):
    slowa_romantycznosc.remove('')
while ('—' in slowa_romantycznosc):
    slowa_romantycznosc.remove('—')

while ('' in slowa_testament_moj):
    slowa_testament_moj.remove('')
while ('—' in slowa_testament_moj):
    slowa_testament_moj.remove('—')

while ('' in slowa_stepy_akremanskie):
    slowa_stepy_akremanskie.remove('')
while ('—' in slowa_stepy_akremanskie):
    slowa_stepy_akremanskie.remove('—')

while ('' in slowa_bogurodzica):
    slowa_bogurodzica.remove('')
while ('—' in slowa_bogurodzica):
    slowa_bogurodzica.remove('—')

while ('' in slowa_cierpeienie):
    slowa_cierpeienie.remove('')
while ('—' in slowa_cierpeienie):
    slowa_cierpeienie.remove('—')

print(slowa_romantycznosc)