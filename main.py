
import requests
import re
import spacy
from collections import Counter
import matplotlib.pyplot as plt
import sklearn
from wordcloud import WordCloud

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

korpus = []
korpus.append(slowa_romantycznosc)
korpus.append(slowa_bogurodzica)
korpus.append(slowa_stepy_akremanskie)
korpus.append(slowa_cierpeienie)
korpus.append(slowa_testament_moj)
do_analizy = []
lan = spacy.load('pl_core_news_lg')
for _ in korpus:
    do_analizy.append(lan(_))

grammar_freq = []
for i in do_analizy:
    helper = Counter()
    helper.update([token.pos_ for token in helper])
    grammar_freq.append(helper)
print(grammar_freq)
print(grammar_freq[0].values())

counter =0
for _ in grammar_freq:
    plt.plot(grammar_freq[_].keys(),grammar_freq[_].values())
    plt.title(f'Frequency of grammar classes')
    plt.xlabel('grammar class')
    plt.ylabel('Frequency')
    plt.savefig('wykresy/' + str(counter))
    counter+=1
    plt.close()


word_form = []
for _ in korpus:
    ptr = Counter()
    ptr.update([token.tag_ for holder in _])
    word_form.append(ptr)

counter+=1
for _ in word_form:
    plt.plot(word_form[_].keys(),word_form[_].values())
    plt.title(f'Frequency of words form')
    plt.xlabel('form of word')
    plt.ylabel('Frequency')
    plt.savefig('wykresy/' + str(counter))
    counter+=1
    plt.close()

nouns = []
licznik = Counter()
for _ in korpus:
    licznik.update([token.lemma_ for token in _ if token.pos_ == 'NOUN'])
    nouns.append(licznik.most_common(15))

counter+=1
for _ in nouns:
    plt.plot(nouns[_].keys(),nouns[_].values())
    plt.title(f'Frequency of nouns')
    plt.xlabel('noun')
    plt.ylabel('Frequency')
    plt.savefig('wykresy/' + str(counter))
    counter+=1
    plt.close()

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

wyszystkie_rzeczowniki = []
for _ in korpus:
    licznik.update([token.lemma_ for token in _ if token.pos_ == 'NOUN'])
    nouns.append(licznik)
tfidf = []
for _ in wyszystkie_rzeczowniki:
    tfidf.append(''.join(_))

sciana_tekstu = [''.join(_) for _ in wyszystkie_rzeczowniki]
for _ in range(len(korpus)):
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(sciana_tekstu)
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(bow_matrix)
    y = dict(zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[i]))
    wordcloud = WordCloud(width=1920, height=1080, background_color='blue').generate_from_frequencies(y)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"Chmura tagów {_ + 1}")
    plt.show()