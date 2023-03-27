import numpy as np


DatasetName = 'ml-10M100K'
# for FileName in ['/movies.dat', '/ratings.dat', '/tags.dat']:
#     print(FileName)
#     with open('./data/' + DatasetName + FileName, 'r', encoding='utf-8') as f:
#
#         cnt = 0
#         for line in f.readlines():
#             print(line)
#             cnt = cnt + 1
#             if cnt >= 3:
#                 break
MovieRating = {}
id2movie = {}
FileName = './data/' + DatasetName + '/movies.dat'
with open(FileName, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data = line.split('::')
        id = int(data[0])
        name = data[1].split('(')[0]
        year = data[1].split('(')[1].split(')')[0]
        tags = data[2].split('\\')[0].split('|')
        # print(id, name, year, tags)
        id2movie[id] = name
        MovieRating[name] = []
        # break

FileName = './data/' + DatasetName + '/ratings.dat'
cnt = 0
with open(FileName, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data = line.split('::')
        usr = data[0]
        item = int(data[1])
        rating = float(data[2])
        timestamp = data[3].split('\n')[0]
        # print(usr, item, rating, timestamp)
        MovieRating[id2movie[item]].append(rating)

        # cnt = cnt + 1
        # if cnt > 1000:
        #     break

num_movies = len(id2movie)
Ratings = np.zeros((num_movies, 1), dtype=np.float32)
pos_cnt = 0
neg_cnt = 0
for i, j in enumerate(id2movie.values()):
    if len(MovieRating[j]) > 0:
        AverageScore = np.round(np.mean(MovieRating[j]), 1)
        Ratings[i, 0] = AverageScore
        pos_cnt += 1
    else:
        Ratings[i, 0] = np.nan
        neg_cnt += 1

print(pos_cnt)
print(neg_cnt)
np.save('./MovieLens.npy',Ratings)

