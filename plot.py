import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MovieLens
data = np.load('./MovieLens.npy')
plt.title('Average score')
plt.hist(data)
plt.show()
df = pd.DataFrame(data)
# df.dropna(how='any')
print(df.describe())
df.plot.box(title='MovieLens')
plt.show()


# Pirated Sites
DatasetName = 'Pirated Sites'
FileName = './data/' + DatasetName + '/movies_dataset.csv'
df = pd.read_csv(FileName)
print(df['IMDb-rating'].describe())
plt.title('Average score')
plt.hist(df['IMDb-rating'])
plt.show()

df['IMDb-rating'].plot.box(title='Pirated Sites')
plt.show()


