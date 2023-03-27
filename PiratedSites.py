import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DatasetName = 'Pirated Sites'
FileName = './data/' + DatasetName + '/movies_dataset.csv'
df = pd.read_csv(FileName)
# print(df.iloc[20543])
# print(df['IMDb-rating'].mode())
# df['IMDb-rating']=df['IMDb-rating'].fillna(value=6.6)
# print(df.iloc[20543])
# plt.title('Average score')
# plt.hist(df['IMDb-rating'])
# plt.show()
language_avg = {}
for language in df['language'].unique():
    df1 = df[(df['language'] == language)]
    mean = np.round(df1['IMDb-rating'].mean(),1)
    language_avg[language]=mean
a = np.array(pd.isna(df['IMDb-rating']))
lis = a.nonzero()[0].tolist()
for i in lis:
    language = df.loc[i]['language']
    df.loc[i,'IMDb-rating']=language_avg[language]

plt.title('Average score')
plt.hist(df['IMDb-rating'])
plt.show()