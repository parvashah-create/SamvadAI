import nlpaug.augmenter.char as nac

text = "The quick brown fox jumps over the lazy dog."


aug = nac.OcrAug()
augmented_texts = aug.augment(text, n=3)
print("Original:")
print(text)
print("Augmented Texts:")
print(augmented_texts)