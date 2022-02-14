# %%
from operator import index
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
import os


#%%
wordle = pd.read_csv('./data/wordle.csv.zip', sep=',', encoding="utf-8", index_col=0)
wordle.sort_values(['peso', 'count'], ascending=False, inplace=True)
w = wordle
w.head(30).sort_values(['count'], ascending=False)




#%%
sim = 'ri'
nao = 'aseght'
posicao_sim = ['r','','','','']
posicao_nao = ['','i','i','','']


r = wordle
for c in sim:
    r = r[r[c]]

for c in nao:
    r = r[~r[c]]

p = 0
for c in posicao_sim:
    p += 1
    if c != '':
        r = r[r[c+str(p)]]
        
p = 0
for chars in posicao_nao:
    p += 1
    for c in chars:
        r = r[~r[c+str(p)]]

print('Quantidade de palavras possíveis', r.shape[0])
print('Top 30')
r.head(30).sort_values(['count'], ascending=False)
# %%
