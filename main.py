import requests
import string
import re
from collections import Counter
import matplotlib as plt
# zimportowanie ksiazek w formacie json
ksiazka_aniol = requests.get('https://wolnelektury.pl/media/book/txt/aniol.txt')
ksiazka_poetyka = requests.get('https://wolnelektury.pl/media/book/txt/arystoteles-poetyka.txt')
ksiazka_pies_barkeselvilow = requests.get('https://wolnelektury.pl/media/book/txt/pies-baskervilleow.txt')
ksiazka_grozny_cien = requests.get('https://wolnelektury.pl/media/book/txt/grozny-cien.txt')
ksiazka_dolina_trwogi = requests.get('https://wolnelektury.pl/media/book/txt/doyle-dolina-trwogi.txt')
# utworzenie pliku bag-of-chars
bag_of_chars = open('bag-of-chars.txt','w')
# zmienna place holder ustawiona na wartosc ASCII odpowiadajaca A
_ = 65
# zliczenie wystepowania wielkich liter wystepujacych w tekstach i napisanie litery - ilosci
while _ <= 90:
    bag_of_chars.write(chr(_))
    bag_of_chars.write(' - ')
    bag_of_chars.write(str(ksiazka_aniol.text.count(chr(_))+
        ksiazka_pies_barkeselvilow.text.count(chr(_))+
        ksiazka_grozny_cien.text.count(chr(_))+
        ksiazka_poetyka.text.count(chr(_))+
        ksiazka_dolina_trwogi.text.count(chr(_))))
    bag_of_chars.writelines('\n')
    _+=1
_ = 97
# zliczenie wystepowania malych liter wystepujacych w tekstach i napisanie litery - ilosci
while _ <= 122:
    bag_of_chars.write(chr(_))
    bag_of_chars.write(' - ')
    bag_of_chars.write(str(ksiazka_aniol.text.count(chr(_))+
        ksiazka_pies_barkeselvilow.text.count(chr(_))+
        ksiazka_grozny_cien.text.count(chr(_))+
        ksiazka_poetyka.text.count(chr(_))+
        ksiazka_dolina_trwogi.text.count(chr(_))))
    bag_of_chars.writelines('\n')
    _+=1

bag_of_words = open('bag-of-words.txt','w')

# podzial ksiazek na slowa ( rozdzielenie przez spacje formanty tekstu oraz utworzenie listy slow )
slowa_aniol = re.split(r'[\r\n\s\.\,\;\:]',ksiazka_aniol.text)
slowa_poetyka = re.split(r'[\r\n\s\.\,\;\:]',ksiazka_poetyka.text)
slowa_pies_bareselvilow = re.split(r'[\r\n\s\.\,\;\:]',ksiazka_pies_barkeselvilow.text)
slowa_dolina_trwogi = re.split(r'[\r\n\s\.\,\;\:]',ksiazka_dolina_trwogi.text)
slowa_grozny_cien = re.split(r'[\r\n\s\.\,\;\:]',ksiazka_grozny_cien.text)
# utworzenie slownikow z czestoscia wystepowania
slownik_aniol = {}
slownik_poetyka = {}
slownik_pies_bareselvilow = {}
slownik_dolina_trwogi = {}
slownik_grozny_cien = {}
for slowo in slowa_aniol:
    slownik_aniol[slowo] = slowa_aniol.count(slowo)
for slowo in slowa_poetyka:
    slownik_poetyka[slowo] = slowa_poetyka.count(slowo)
for slowo in slowa_pies_bareselvilow:
    slownik_pies_bareselvilow[slowo] = slowa_pies_bareselvilow.count(slowo)
for slowo in slowa_dolina_trwogi:
    slownik_dolina_trwogi[slowo] = slowa_dolina_trwogi.count(slowo)
for slowo in slowa_grozny_cien:
    slownik_grozny_cien[slowo] = slowa_grozny_cien.count(slowo)
del slownik_aniol['']
del slownik_poetyka['']
del slownik_pies_bareselvilow['']
del slownik_dolina_trwogi['']
del slownik_grozny_cien['']
#
# all_dicts = [
#     slownik_aniol,
#     slownik_poetyka,
#     slownik_pies_bareselvilow,
#     slownik_dolina_trwogi,
#     slownik_grozny_cien
# ]
# counters = [Counter(dictionary) for dictionary in all_dicts]
# merged_counter = counters[0]
# for counter in counters[1:]:
#     merged_counter.update(counter)
# korpus = dict(merged_counter)
# korpus = dict(sorted(korpus.items(), key= lambda item: item[1],reverse=True))
# for key, value in korpus.items():
#     bag_of_words.write(f'{key}:{value}\n')

def term_frequency(dictionary):
    sum_values = 0
    for key,value in dictionary.items():
        sum_values += value
    tf = {}
    for key,value in dictionary.items():
        tf[key] = value/sum_values
    return tf

aniol_tf = term_frequency(slownik_aniol)
print(aniol_tf)