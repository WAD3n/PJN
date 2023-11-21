import requests
import string
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math

stop_words = open('stopwords','r')
x = stop_words.readlines()
_ = 0
list_of_stop_words = []
while _ < len(x):
    if _ < len(x)-1:
        z=x[_].split('\n')
        z.pop(1)
        list_of_stop_words.append(z)
        _ += 1
    else:
        list_of_stop_words.append(x[_])
        break

# zimportowanie ksiazek w formacie json
ksiazka_aniol = requests.get('https://wolnelektury.pl/media/book/txt/aniol.txt')
ksiazka_poetyka = requests.get('https://wolnelektury.pl/media/book/txt/arystoteles-poetyka.txt')
ksiazka_pies_barkeselvilow = requests.get('https://wolnelektury.pl/media/book/txt/pies-baskervilleow.txt')
ksiazka_grozny_cien = requests.get('https://wolnelektury.pl/media/book/txt/grozny-cien.txt')
ksiazka_dolina_trwogi = requests.get('https://wolnelektury.pl/media/book/txt/doyle-dolina-trwogi.txt')
# utworzenie pliku bag-of-chars
#bag_of_chars = open('bag-of-chars.txt','w')
# zmienna place holder ustawiona na wartosc ASCII odpowiadajaca A
_ = 65
# zliczenie wystepowania wielkich liter wystepujacych w tekstach i napisanie litery - ilosci
# while _ <= 90:
#     bag_of_chars.write(chr(_))
#     bag_of_chars.write(' - ')
#     bag_of_chars.write(str(ksiazka_aniol.text.count(chr(_))+
#         ksiazka_pies_barkeselvilow.text.count(chr(_))+
#         ksiazka_grozny_cien.text.count(chr(_))+
#         ksiazka_poetyka.text.count(chr(_))+
#         ksiazka_dolina_trwogi.text.count(chr(_))))
#     bag_of_chars.writelines('\n')
#     _+=1
# _ = 97
# # zliczenie wystepowania malych liter wystepujacych w tekstach i napisanie litery - ilosci
# while _ <= 122:
#     bag_of_chars.write(chr(_))
#     bag_of_chars.write(' - ')
#     bag_of_chars.write(str(ksiazka_aniol.text.count(chr(_))+
#         ksiazka_pies_barkeselvilow.text.count(chr(_))+
#         ksiazka_grozny_cien.text.count(chr(_))+
#         ksiazka_poetyka.text.count(chr(_))+
#         ksiazka_dolina_trwogi.text.count(chr(_))))
#     bag_of_chars.writelines('\n')
#     _+=1

#bag_of_words = open('bag-of-words.txt','w')

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
    slownik_aniol[slowo] = 0
for slowo in slowa_poetyka:
    slownik_poetyka[slowo] = 0
for slowo in slowa_pies_bareselvilow:
    slownik_pies_bareselvilow[slowo] = 0
for slowo in slowa_dolina_trwogi:
    slownik_dolina_trwogi[slowo] = 0
for slowo in slowa_grozny_cien:
    slownik_grozny_cien[slowo] = 0


for slowo in slowa_aniol:
    if slowo in list_of_stop_words: continue
    slownik_aniol[slowo] = slowa_aniol.count(slowo)
for slowo in slowa_poetyka:
    if slowo in list_of_stop_words: continue
    slownik_poetyka[slowo] = slowa_poetyka.count(slowo)
for slowo in slowa_pies_bareselvilow:
    if slowo in list_of_stop_words: continue
    slownik_pies_bareselvilow[slowo] = slowa_pies_bareselvilow.count(slowo)
for slowo in slowa_dolina_trwogi:
    if slowo in list_of_stop_words: continue
    slownik_dolina_trwogi[slowo] = slowa_dolina_trwogi.count(slowo)
for slowo in slowa_grozny_cien:
    if slowo in list_of_stop_words: continue
    slownik_grozny_cien[slowo] = slowa_grozny_cien.count(slowo)
del slownik_aniol['']
del slownik_poetyka['']
del slownik_pies_bareselvilow['']
del slownik_dolina_trwogi['']
del slownik_grozny_cien['']
# all_dicts = [
#      slownik_aniol,
#      slownik_poetyka,
#      slownik_pies_bareselvilow,
#      slownik_dolina_trwogi,
#      slownik_grozny_cien
#  ]
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

def inverse_document_frequency(dictionary,d2,d3,d4,d5):
    file = open('bag-of-words.txt','r')
    idf = {}
    occurence_in_files = 1
    for key,value in dictionary.items():
        if key in d2.keys():occurence_in_files  += 1
        if key in d3.keys(): occurence_in_files += 1
        if key in d4.keys(): occurence_in_files += 1
        if key in d5.keys(): occurence_in_files += 1
        idf[key] = abs(np.log( 5 / occurence_in_files))
        occurence_in_files = 1
    return idf
def tf_idf(dictionary,tf,idf):
    tf_wartosci = list(tf.values())
    idf_wartosci = list(idf.values())
    ptr = {}
    _ = 0
    for key , value in dictionary.items():
        ptr[key] =tf_wartosci[_] * idf_wartosci[_]
        _ += 1
    _ = 0
    return ptr

def draw_zipf_graph(dictionary,nazwa : string):
    dictionary = dict(sorted(dictionary.items(), key= lambda item:item[1], reverse= True))
    del dictionary['—']
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    ptr = []
    ptr1 = []
    for _ in range(10):
        ptr.append(values[_]/(_+1))
        ptr1.append(keys[_])
    plt.plot(ptr1, ptr)
    plt.title(f'Zipf Graph')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.savefig('wykresy/' + nazwa)
    plt.close()

draw_zipf_graph(slownik_aniol,'aniol')
draw_zipf_graph(slownik_poetyka,'poetyka')
draw_zipf_graph(slownik_pies_bareselvilow,'pies')
draw_zipf_graph(slownik_grozny_cien,'grozny')
draw_zipf_graph(slownik_dolina_trwogi,'dolina')


aniol_tf = term_frequency(slownik_aniol)
grozny_tf = term_frequency(slownik_grozny_cien)
pies_tf = term_frequency(slownik_pies_bareselvilow)
dolina_tf = term_frequency(slownik_pies_bareselvilow)
poetyka_tf = term_frequency(slownik_poetyka)


aniol_idf = inverse_document_frequency(slownik_aniol,slownik_poetyka,slownik_pies_bareselvilow,slownik_grozny_cien,slownik_dolina_trwogi)
grozny_idf = inverse_document_frequency(slownik_grozny_cien,slownik_poetyka,slownik_pies_bareselvilow,slownik_aniol,slownik_dolina_trwogi)
pies_idf = inverse_document_frequency(slownik_pies_bareselvilow,slownik_poetyka,slownik_aniol,slownik_grozny_cien,slownik_dolina_trwogi)
dolina_idf = inverse_document_frequency(slownik_dolina_trwogi,slownik_poetyka,slownik_pies_bareselvilow,slownik_grozny_cien,slownik_aniol)
poetyka_idf = inverse_document_frequency(slownik_poetyka,slownik_aniol,slownik_pies_bareselvilow,slownik_grozny_cien,slownik_dolina_trwogi)

# MACIERZE TF_IDF
aniol_matrix = tf_idf(slownik_aniol,aniol_tf,aniol_idf)
grozny_matrix = tf_idf(slownik_grozny_cien,grozny_tf,grozny_idf)
pies_matrix = tf_idf(slownik_pies_bareselvilow,pies_tf,pies_idf)
#dolina_matrix = tf_idf(slownik_dolina_trwogi,dolina_tf,dolina_idf)
poetyka_matrix = tf_idf(slownik_poetyka,poetyka_tf,poetyka_idf)

def odleglosc_cos(matrix1,matrix2):
    distance = 0
    sum = 0
    sumx_squere = 0
    sumy_squere = 0
    matrix1_values = list(matrix1.values())
    matrix2_values = list(matrix2.values())
    if len(matrix1_values) > len(matrix2_values):
        for i in range(len(matrix2_values)):
            sum += matrix1_values[i]*matrix2_values[i]
            sumx_squere += pow(matrix1_values[i],2)
            sumy_squere += pow(matrix2_values[i],2)
    else:
        for i in range(len(matrix1_values)):
            sum += matrix1_values[i] * matrix2_values[i]
            sumx_squere += pow(matrix1_values[i], 2)
            sumy_squere += pow(matrix2_values[i], 2)
    mianownik = (math.sqrt(sumx_squere)*math.sqrt(sumy_squere))
    if mianownik != 0:
        distance = sum/mianownik
    else:
        distance = sum/1
    return distance

aniol_grozny_od = odleglosc_cos(aniol_matrix,grozny_matrix)
aniol_pies_od = odleglosc_cos(aniol_matrix,pies_matrix)
aniol_poetyka_od = odleglosc_cos(aniol_matrix,poetyka_matrix)

grozny_pies_od = odleglosc_cos(grozny_matrix, pies_matrix)
grozny_poetyka_od = odleglosc_cos(grozny_matrix, poetyka_matrix)

pies_poetyka_od = odleglosc_cos(pies_matrix,poetyka_matrix)

odleglosci = [[None,'aniol','grozny','pies','poetyka'],
              ['aniol',None,aniol_grozny_od.__round__(2),aniol_pies_od.__round__(2),aniol_poetyka_od.__round__(2)],
              ['grozny',aniol_grozny_od.__round__(2),None,grozny_pies_od.__round__(2),grozny_poetyka_od.__round__(2)],
              ['pies',aniol_pies_od.__round__(2),grozny_pies_od.__round__(2),None,pies_poetyka_od.__round__(2)],
              ['poetyka',aniol_poetyka_od.__round__(2),grozny_poetyka_od.__round__(2),pies_poetyka_od.__round__(2),None]]

for x in odleglosci:
    print(x,'\n')

