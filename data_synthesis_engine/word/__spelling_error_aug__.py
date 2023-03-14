import nlpaug.augmenter.word as naw

text = "The quick brown fox jumps over the lazy dog"

aug = naw.SpellingAug()
augmented_texts = aug.augment(text, n=1)
print("Original:")
print(text)
print("Augmented Texts:")
print(augmented_texts)