import pandas as pd

# 读取两个原始CSV文件
new_data_df = pd.read_csv('./data/new_data.csv')
shixi_data_df = pd.read_csv('./data/shixi.csv')

# 假设两份数据的列名完全一致，首先创建一个新的DataFrame，其内容是new_data_df的所有数据，并添加新列'shixiclassify'
new_data_with_classify = new_data_df.copy()
new_data_with_classify['shixi_classify'] = 0  # 初始化新列为0

# 对比两个数据集中id列相同的行，并在新列'shixiclassify'下标记为1
for index, row in new_data_with_classify.iterrows():
    if row['id'] in shixi_data_df['id'].values:
        new_data_with_classify.at[index, 'shixi_classify'] = 1

# 将处理后的新数据写入新的CSV文件
new_data_with_classify.to_csv('./data/shixi_classify.csv', index=False)