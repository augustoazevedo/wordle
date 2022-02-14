# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), '.'))
    print(os.getcwd())
except:
    pass
# %%
from IPython import get_ipython


# %%
import pandas as pd
import numpy as np
import io
import os
import zlib
import glob
from functools import reduce


#%%
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_count = {}
for c in alphabet:
    char_count[c] = 0
# %%

#%%
english_words = pd.read_csv('./data/words_alpha.txt.zip', names=['word'])
english_words = english_words[english_words.word.str.len() == 5].reset_index(drop=True)
english_words

#%%
english_words_freq = pd.read_csv('./data/freq.csv.zip')
english_words_freq

#%%
english_words = english_words.join(english_words_freq.set_index('word'), on='word')
english_words


#%%
for word in english_words.word:
    for char in word:
        char_count[char] += 1

char_count

#%%
df = english_words
df['peso'] = df.word.apply(lambda w: reduce(lambda soma, c: soma + char_count[c], list(set(w)), 0 ))
df.sort_values(['peso'], ascending=False)


#%%
for c in alphabet:
    df[c] = df.word.apply(lambda w: w.find(c) != -1)

for c in alphabet:
    for position in [1,2,3,4,5]:
        df[c + str(position)] = df.word.apply(lambda w: w[position -1] == c)

df


#%%
df.to_csv('./data/wordle.csv.zip', compression='zip', sep=',', encoding="utf-8")

# %%
