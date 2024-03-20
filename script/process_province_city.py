import jionlp as jio
import pandas as pd

# text = '上海闵行区兴迪商务大厦603'
# res = jio.parse_location(text)
# print(res)

df = pd.read_csv('data/new_data.csv')

# 定义一个函数，用于解析地址并返回省、市、县
def parse_address(address):
    try:
        result = jio.parse_location(address)
        return result['province'], result['city'], result['county']
    except Exception as e:
        # 如果解析出现问题，返回空值
        return None, None, None

# 应用函数到address列
df[['province', 'city', 'county']] = df.apply(lambda row: pd.Series(parse_address(row['address'])), axis=1)

new_df = df[['id', 'company', 'province', 'city', 'county']]

# 将更新后的DataFrame保存到新的CSV文件
new_df.to_csv('data/data_processed_address.csv', index=False)

