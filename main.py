import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('naglowki','r') as plik:
    naglowki = plik.read()

naglowki = naglowki.split('\n')
print(naglowki)

polski = spacy.load('pl_core_news_sm')
stop_list = polski.Defaults.stop_words

lemantyzacja = []
for _ in range(len(naglowki)):
    naglowek = polski(naglowki[_])
    lemantyzacja.append(' '.join([token.lemma_ for token in naglowek if token.lemma_.isalpha()]))

print(lemantyzacja)
for _ in stop_list:
    if _ in lemantyzacja:
        lemantyzacja.remove(_)
vectorizer = TfidfVectorizer(smooth_idf=True)
X = vectorizer.fit_transform(lemantyzacja)
words = vectorizer.get_feature_names_out()
X = X.toarray()
X.shape

num_topics = 3


svd = TruncatedSVD(n_components=num_topics)
U = svd.fit_transform(X)
S = svd.singular_values_
Vt = svd.components_
U = normalize(U, axis=0)

U = np.array(U)
S = np.array(S)
Vt = np.array(Vt)
(U, S, Vt)

word_tfidf = dict(zip(words, Vt[0]))
wordcloud = WordCloud(width=1900, height=1000, background_color='white').generate_from_frequencies(word_tfidf)
plt.figure(figsize=(19, 11))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.jpg')

word_tfidf = dict(zip(words, Vt[2]))
wordcloud = WordCloud(width=1900, height=1000, background_color='white').generate_from_frequencies(word_tfidf)
plt.figure(figsize=(19, 11))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud2.jpg')

U_normalized = normalize(U, axis=1, norm='l2')

def show_radar(document_index, num_topics):
    angles = np.linspace(0, 2 * np.pi, num_topics, endpoint=False).tolist()
    angles += angles[:1]
    values = U_normalized[document_index].tolist()
    values += values[:1]
    plt.figure(figsize=(6, 6))
    plt.polar(angles, values, marker='o')
    plt.fill(angles, values, alpha=0.25)
    plt.title(f"Dokument {document_index+1}")
    plt.xticks(angles[:-1], [f'Temat {i+1}' for i in range(num_topics)])
    plt.savefig('radar'+f'{document_index}')

show_radar(0, num_topics)
show_radar(1, num_topics)
show_radar(2, num_topics)
show_radar(3, num_topics)
show_radar(4, num_topics)
show_radar(5, num_topics)
show_radar(6, num_topics)
