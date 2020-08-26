import os 
import pandas as pd

fakes = os.listdir('./fake/')
trues = os.listdir('./true/')

fakenews = []
fakenewsf = []

for f in fakes:
  fd = open('./fake/' + f, 'r')
  t = fd.read()
  fakenews.append(t)
  fakenewsf.append('fake')

d = {'text' : fakenews, 'category' : fakenewsf}
df = pd.DataFrame(data=d)

print(df.head())

