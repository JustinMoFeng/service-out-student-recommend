import pandas as pd
from pprint import pprint
import re

data = pd.read_csv('./data/new_data.csv', header='infer', delimiter=',', encoding='utf-8')
data.fillna('', inplace=True)
array = data.values

# 找到所有的实习
dataSet = set()
for i in range(len(array)):
    # 如果array[i][5]中包含'实习'，则将这一条放入dataSet中】
    pattern = '实习[^经期工项0123456789]'
    pattern = re.compile(pattern)
    if re.search(pattern, array[i][5]) is not None or '实习' in array[i][1]:
        dataSet.add(i)

# 按照dataSet中的序号进行查找，将其中包含编号的信息存入csv
newData = []
for i in dataSet:
    newData.append(array[i])

# 将newData存入csv
newData = pd.DataFrame(newData, columns=data.columns)
newData.to_csv('./data/shixi.csv', index=False, encoding='utf-8')