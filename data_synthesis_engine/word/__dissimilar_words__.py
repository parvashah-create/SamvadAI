import spacy
import nltk
from nltk.corpus import wordnet
import random

nlp = spacy.load("en_core_web_lg")
nltk.download('wordnet')

# Define function to get similar word from WordNet

def get_antonym(word):
    """
    Returns the antonym of the given word, if available, or the original word otherwise.
    """
    # Get the synsets for the word
    synsets = wordnet.synsets(word)

    # Check if any of the synsets have antonyms
    for synset in synsets:
        antonyms = [antonym.name() for lemma in synset.lemmas() for antonym in lemma.antonyms()]
        if antonyms:
            # Return the first antonym found
            return random.choice(antonyms)

    # If no antonyms were found, return the original word
    return word



# function to convert sentence to similar sentence
def dissimilar_word_sentence(sentence):

    # Parse sentence using spaCy
    doc = nlp(sentence)

    # Iterate through tokens in sentence
    new_sentence = []
    for token in doc:
        if token.pos_ in ["VERB", "ADJ"]:
            # Get similar word from WordNet and append to new sentence
            new_word = get_antonym(token.text)
            new_sentence.append(new_word)
        else:
            # Append original word to new sentence
            new_sentence.append(token.text)

    # Join words in new sentence into a string
    new_sentence_str = " ".join(new_sentence)
    return new_sentence_str
