import pandas as pd
from pprint import pprint

data = pd.read_csv('./data/new_data.csv', header='infer', delimiter=',', encoding='utf-8')
data.fillna('', inplace=True)
array = data.values

# 找到所有的职业描述
dataList = []
for i in range(len(array)):
    dataList.append(array[i][5])

# 将dataList存入csv
dataList = pd.DataFrame(dataList, columns=['职业描述'])
dataList.to_csv('./data/description.csv', index=False, encoding='utf-8')