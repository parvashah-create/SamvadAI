import spacy
import nltk
from nltk.corpus import wordnet
import random

nlp = spacy.load("en_core_web_lg")
nltk.download('wordnet')

# Define function to get similar word from WordNet
def get_similar_word(word):
    """
    Returns a similar word from WordNet
    """
    synsets = wordnet.synsets(word)
    if synsets:
        # Get all lemmas for all synsets of the word
        lemmas = [l for s in synsets for l in s.lemmas()]
        if lemmas:
            # Get all names for all lemmas, excluding the original word
            names = set(l.name() for l in lemmas if l.name() != word)
            if names:
                # Choose a random name from the set of names
                return random.choice(list(names))
    # If no similar word is found, return the original word
    return word

# function to convert sentence to similar sentence
def similar_word_sentence(sentence):

    # Parse sentence using spaCy
    doc = nlp(sentence)

    # Iterate through tokens in sentence
    new_sentence = []
    for token in doc:
        if token.pos_ in ["VERB", "ADJ"]:
            # Get similar word from WordNet and append to new sentence
            new_word = get_similar_word(token.text)
            new_sentence.append(new_word)
        else:
            # Append original word to new sentence
            new_sentence.append(token.text)

    # Join words in new sentence into a string
    new_sentence_str = " ".join(new_sentence)
    return new_sentence_str






# Substitute similar words using GloVe

import gensim.downloader as api

 

def similar_glove_word(sentence):
    # Parse sentence using spaCy
    doc = nlp(sentence)
    model = api.load('glove-twitter-25') 
    # Iterate through tokens in sentence
    new_sentence = []
    for token in doc:
        if token.pos_ in ["VERB", "ADJ"]:
            # Get similar word from GloVe and append to new sentence
            try:
                similar_words = model.most_similar(token.text.lower(), topn=5)
                print(token,similar_words)
                new_word = similar_words[0][0] # Get the most similar word
                new_sentence.append(new_word)
            except KeyError:
                # If the word is not in the GloVe model, append original word
                new_sentence.append(token.text)
        else:
            # Append original word to new sentence
            new_sentence.append(token.text)

    # Join words in new sentence into a string
    new_sentence_str = " ".join(new_sentence)
    return new_sentence_str



# For testing purposes
# text = "The quick brown fox jumps over the lazy dog."
# print(similar_glove_word(text))