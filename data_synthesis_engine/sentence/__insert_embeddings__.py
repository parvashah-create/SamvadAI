from transformers import pipeline




fill_masker = pipeline(model="bert-base-uncased")
print(fill_masker("This is a simple [MASK]."))



# import spacy
# from transformers import pipeline

# nlp = spacy.load('en_core_web_sm')
# fill_mask = pipeline('fill-mask', model='bert-base-uncased')

# def fill_prepositions(sentence):
#     # Parse the sentence with Spacy
#     doc = nlp(sentence)
    
#     # Check if there are any prepositions in the sentence
#     has_prepositions = any(token.pos_ == 'ADP' for token in doc)
    
#     # If there are no prepositions, return the original sentence
#     if not has_prepositions:
#         return sentence
    
#     # Loop through each token in the sentence
#     new_sentence = ''
#     for token in doc:
#         if token.pos_ == 'ADP': # If the token is a preposition
#             new_sentence += '[MASK] ' # Replace it with [MASK]
#         else:
#             new_sentence += token.text + ' '
    
#     # Use the fill-mask pipeline to fill in the [MASK]
#     result = fill_mask(new_sentence.strip())
    
#     # Return the top prediction for the masked token
#     return result

# sentence = 'I went to the store with my friend.'
# result = fill_prepositions(sentence)
# print(result) # Output: "I went [MASK] the store with my friend."