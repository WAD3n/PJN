import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import path
import gensim.downloader as api
import nltk
from gensim.models import KeyedVectors
!git clone  https://github.com/mmazurek-wat/nlp-resources-edu.git
resource_path = '/content/nlp-resources-edu/05_Embedding_lab/'
sys.path.append(resource_path)
capitals_file = 'capitals.txt'
capitals_file_path = path.join(resource_path, capitals_file)
data = pd.read_csv(capitals_file_path, delimiter=' ')
data.columns = ['city1', 'country1', 'city2', 'country2']
data.head(5)
embeddings = api.load('word2vec-google-news-300')
vec_king = embeddings['king']
word_embeddings = {}
for word in embeddings.key_to_index:
    word_embeddings[word] = embeddings[word]
print(len(word_embeddings))
embedding_subset_file = 'word_embeddings_subset.p'
embedding_subset_file_path = path.join(resource_path, embedding_subset_file)
word_embeddings = pickle.load(open(embedding_subset_file_path, "rb"))
len(word_embeddings)
print(* word_embeddings.keys())
print("dimension: {}".format(word_embeddings['Spain'].shape[0]))
def cosine_similarity(A, B):
    dot = np.dot(A, B)
    norma = np.linalg.norm(A) 
    normb = np.linalg.norm(B) 
    cos = dot / (norma * normb) 
    return cos
king = word_embeddings['king']
queen = word_embeddings['queen']
cosine_similarity(king, queen)

def euclidean(A, B):
    d = np.linalg.norm(A - B)
      return d
euclidean(king, queen)

def get_country(city1, country1, city2, embeddings):

    group = set((city1, country1, city2))
    city1_emb = embeddings[city1]
    country1_emb = embeddings[country1]
    city2_emb = embeddings[city2]
    vec = country1_emb - city1_emb + city2_emb
    similarity = -1
    country = ''
    for word in embeddings.keys():
        if word not in group:
            word_emb = embeddings[word]
            cur_similarity = cosine_similarity(vec, word_emb)
            if cur_similarity > similarity:
                similarity = cur_similarity
                country = (word, similarity)
    return country

get_country('Athens', 'Greece', 'Cairo', word_embeddings)

def get_accuracy(word_embeddings, data):
    num_correct = 0
    for i, row in data.iterrows():
        city1 = row['city1']
        country1 = row['country1']
        city2 =  row['city2']
        country2 = row['country2']
        predicted_country2, _ = get_country(city1, country1, city2, word_embeddings)
        if predicted_country2 == country2:
            num_correct += 1
    m = len(data)
    accuracy = num_correct / m
    return accuracy
def find_closest_word(v, embeddings):
    closest_word = None 
    smallest_distance = float('inf') 
    for word in embeddings.keys():
        word_embedding = embeddings[word]
        distance = euclidean(v, word_embedding) 
        if distance < smallest_distance:
            smallest_distance = distance 
            closest_word = word 
    return closest_word

def get_analogy(rel_src1, rel_trg1, rel_src2):
  analogies = {
      ('Man', 'King', 'Woman'): 'Queen',
      ('fast', 'slow', 'clever'): 'dull',
  }
  return analogies.get((rel_src1, rel_trg1, rel_src2))
rel=('fast', 'slow', 'clever')
print(get_analogy(rel[0], rel[1], rel[2]))
