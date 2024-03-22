from pprint import pprint
from paddlenlp import Taskflow
import pandas as pd

# schema = ['时间', '选手', '赛事名称'] # Define the schema for entity extraction
# ie = Taskflow('information_extraction', schema=schema)
# pprint(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")) # Better print results using pprint

df = pd.read_csv('data/new_data.csv')

schema = ['编程语言', '框架', '工具', '技术','数据库']
ie = Taskflow('information_extraction', schema=schema, use_gpu=True, batch_size=1,position_prob=0.05)

from tqdm import tqdm
import time

def find_tech_stack_for_word_with_progress(text):
    result = ie(text)
    time.sleep(0.1)  # 模拟处理时间
    return result

# 创建一个 tqdm 迭代器，用于跟踪处理进度
tqdm_iterator = tqdm(total=len(df), desc="Processing Data")

# 使用 tqdm 迭代器来迭代数据框中的每一行
def process_row(row):
    tech_stack = find_tech_stack_for_word_with_progress(row['description'])
    tqdm_iterator.update(1)  # 更新进度条
    # tech_stack每一项的text组成数组，最后转化为以;分割的字符串
    unique_texts = set()  # 创建一个空集合来存储唯一文本
    for item in tech_stack:
        for entity_list in item.values():
            for entity_dict in entity_list:
                unique_texts.add(entity_dict['text'])  # 将每个文本添加到集合中

    tech_stack_text = ';'.join([item for item in unique_texts])
    # print(tech_stack_text)
    return tech_stack_text

# 将处理函数应用于每一行并将结果添加到新的列中
df['tech_stack'] = df.apply(process_row, axis=1)

# 关闭 tqdm 迭代器
tqdm_iterator.close()

# 保存处理后的数据到 CSV 文件
new_df = df[['id', 'company', 'description', 'tech_stack']]
new_df.to_csv('data/data_processed_tech_stack.csv', index=False)


