import pandas as pd

# 读取CSV文件
df = pd.read_csv('data/data_processed_address.csv')

# 找出所有'province', 'city', 'county'列都为空的行
empty_rows = df[df['province'].isnull() & df['city'].isnull() & df['county'].isnull()]

# 将这些行保存到新的CSV文件中
empty_rows.to_csv('address_empty_rows.csv', index=False)
