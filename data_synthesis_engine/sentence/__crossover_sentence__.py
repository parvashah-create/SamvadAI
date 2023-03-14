import random




# Example texts
text1 = "This is a sentence. This is another sentence. This in one more sentence."
text2 = "This is a sentence 2. This is another sentence 2."

# Split text1 into sentences
sentences1 = text1.split('.')

# Split text2 into sentences
sentences2 = text2.split('.')
sentences1.pop()
sentences2.pop()

# Combine the last sentence of text1 with the last sentence of text2
combined_sentence = sentences1 + sentences2
# shuffle sentences
random.shuffle(combined_sentence)

if len(combined_sentence)%2 == 0:
    n_split =  (len(combined_sentence)/2)-1
else:
    n_split =  ((len(combined_sentence)+1)/2)-1

n_split = int(n_split)

# Remove the last sentence from both texts
sentences1 = combined_sentence[:n_split+1]
sentences2 = combined_sentence[n_split+1:]

# Combine the remaining sentences
new_text1 = '. '.join(sentences1) + '.'
new_text2 = '. '.join(sentences2) + '.'

# Print the new texts
print('New Text 1:', new_text1)
print('New Text 2:', new_text2)