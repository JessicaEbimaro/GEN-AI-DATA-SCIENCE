import pandas as pd
from nltk.tokenize import word_tokenize

df = pd.read_csv("sample.csv", header=None, sep='\r\n', engine='python', names= ['tweets'])

df['lowercase']= df['tweets'].apply(lambda x: (x.lower()))

df['tokens'] = df ['lowercase'].apply(lambda x: word_tokenize(x))
print (df['tokens'])