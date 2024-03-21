import pandas as pd

data = pd.read_csv('./data/description.csv', header='infer', delimiter=',', encoding='utf-8')
data.fillna('', inplace=True)
array = data.values

# 随机选择十条不重复的实习
import random
random.seed(10)
dataSet = set()
while len(dataSet) < 10:
    dataSet.add(random.randint(0, len(array) - 1))

# 将dataSet中的序号对应的信息存入csv
newData = []
for i in dataSet:
    newData.append(array[i])

# 将newData存入csv
newData = pd.DataFrame(newData, columns=data.columns)
newData.to_csv('./data/random_description.csv', index=False, encoding='utf-8')


