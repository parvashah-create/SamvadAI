import nltk
from nltk.corpus import wordnet

def augment_with_synonyms(text, n_augmentations):
    # Tokenize the input text
    tokens = nltk.word_tokenize(text)

    # Loop over each token and replace with a synonym from WordNet
    augmented_texts = []
    for i in range(n_augmentations):
        augmented_tokens = []
        for token in tokens:
            # Find synonyms for the token using WordNet
            synonyms = wordnet.synsets(token)
            if synonyms:
                # Select a random synonym for the token
                synonym = synonyms[0].lemmas()[0].name()
                # Replace the token with the synonym
                augmented_tokens.append(synonym)
            else:
                # If there are no synonyms, keep the original token
                augmented_tokens.append(token)

        # Combine the augmented tokens into a new text string
        augmented_text = ' '.join(augmented_tokens)
        augmented_texts.append(augmented_text)

    return augmented_texts

# Example usage
text = "The quick brown fox jumps over the lazy dog."
augmented_texts = augment_with_synonyms(text, n_augmentations=5)
print(augmented_texts)
