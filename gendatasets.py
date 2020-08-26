# Imports and definitions

import os 
import pandas as pd

# Constants

NUM_NEWS = 3600

# Datasets

metacols = ['author', 'link', 'category', 'publication', 'tokens', 'words', 'types', 'links', 'uppercase', 'verbs', 'subjuntiveimperative', 'nouns', 'adjectives', 'adverbs', 'modalverbs', 'personalpronouns', 'pluralpersonalpronouns', 'pronouns', 'pausality', 'characters', 'sentencelength', 'wordlength', 'speelingerrors', 'emotiveness', 'diversity', 'fake_or_true']
dfmeta = pd.DataFrame(columns = metacols)

# Reading meta information about news

for i in range(1, NUM_NEWS + 1):
    # Reading info from files
    fdf = open('./full_texts/fake-meta-information/' + str(i) + '-meta.txt', 'r')
    linef = [x.strip() for x in fdf.readlines()]
    fdt = open('./full_texts/true-meta-information/' + str(i) + '-meta.txt', 'r')
    linet = [x.strip() for x in fdt.readlines()]
    # Organizing tuples
    dflinef = dict(zip(metacols, linef))
    dflinef['fake_or_true'] = 0
    dflinet = dict(zip(metacols, linet))
    dflinet['fake_or_true'] = 1
    # Appending data
    dfmeta = dfmeta.append(dflinef, ignore_index=True)
    dfmeta = dfmeta.append(dflinet, ignore_index=True)

dfmeta.head(100).to_csv('./csv/meta_info_100.csv', index=False)
dfmeta.to_csv('./csv/meta_info.csv', index=False)

# Reading full text news

news = []
newsc = []

for i in range(1, NUM_NEWS + 1):
  # Reading news files
  fdf = open('./full_texts/fake/' + str(i) + '.txt', 'r')
  newsf = fdf.read()
  fdt = open('./full_texts/true/' + str(i) + '.txt', 'r')
  newst = fdt.read()
  news.append(newsf)
  newsc.append(0)
  news.append(newst)
  newsc.append(1)

dfnews = pd.DataFrame(data = {'news': news, 'fake_or_true': newsc})

dfnews.head(100).to_csv('./csv/news_full_100.csv', index=False)
dfnews.to_csv('./csv/news_full.csv', index=False)

# Reading size normalized text news

snnews = []
snnewsc = []

for i in range(1, NUM_NEWS + 1):
  # Reading news files
  fdf = open('./size_normalized_texts/fake/' + str(i) + '.txt', 'r')
  newsf = fdf.read()
  fdt = open('./size_normalized_texts/true/' + str(i) + '.txt', 'r')
  newst = fdt.read()
  snnews.append(newsf)
  snnewsc.append(0)
  snnews.append(newst)
  snnewsc.append(1)

dfnewssn = pd.DataFrame(data = {'news': snnews, 'fake_or_true': snnewsc})

dfnewssn.head(100).to_csv('./csv/news_sn_100.csv', index=False)
dfnewssn.to_csv('./csv/news_sn.csv', index=False)


