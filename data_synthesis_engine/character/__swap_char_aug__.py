import nlpaug.augmenter.char as nac

text = "The quick brown fox jumps over the lazy dog."


aug = nac.RandomCharAug(action="swap")
augmented_text = aug.augment(text)
print("Original:")
print(text)
print("Augmented Text:")
print(augmented_text)