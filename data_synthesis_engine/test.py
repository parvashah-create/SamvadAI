from __similar_words__ import similar_word_sentence
import json
import pandas as pd
from __dissimilar_words__ import dissimilar_word_sentence
from back_translation import back_translater
# # Define sample sentence
# sentence = "The quick brown fox jumps over the lazy dog."
# # Print original and new sentence
# text = similar_word_sentence(sentence)
# print(text)

# # Read the JSON lines file into a list of dictionaries
data = []
with open('data_synthesis_engine/dynasent-v1.1-round01-yelp-dev.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))



# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data)

exp_df = df[["sentence","model_0_label"]]
test_df = exp_df.sample(n=25)
reword_sentence = []

for text in test_df["sentence"]:
    # reworded = dissimilar_word_sentence(text)
    es_en, de_en, ja_en, fr_en = back_translater(text)
    reword_sentence.append([es_en, de_en, ja_en, fr_en])

test_df[["es_en","de_en", "ja_en", "fr_en"]] = reword_sentence
test_df.to_csv("test1_df.csv")
print(test_df)

