import nlpaug.augmenter.word as naw



# function yo get augmented texts
def insert_contextual_words(text,no_augs):
    # nlp aug word augmentor 
    aug = naw.ContextualWordEmbsAug(
        model_path='bert-base-uncased', action="insert")
    # get augmented texts
    augmented_text = aug.augment(text, n=no_augs)
    
    return augmented_text




# Test the above function
# text = "The quick brown fox jumps over the lazy dog."
# print(insert_contextual_words(text,2))

