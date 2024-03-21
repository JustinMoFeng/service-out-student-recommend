import pandas as pd

df = pd.read_csv('data/new_data.csv')

def calculate_year_salary(salary):
    # 检查salary是否为"面议"
    if salary == '面议':
        return "0-0"
    # 如果salary包含'薪'，则按照原有逻辑处理
    if '薪' in salary: 
        try:
            base_salary, multiplier = salary.split('·')
            low, high = base_salary.split('-')
            low = int(low.replace('K', '')) * int(multiplier.replace('薪', ''))
            high = int(high.replace('K', '')) * int(multiplier.replace('薪', ''))
        except ValueError:
            print(f"薪资格式错误: {salary}")
            return None
    else:
        try:
            low, high = salary.split('-')
            low = int(low.replace('K', '')) * 12
            high = int(high.replace('K', '')) * 12
        except ValueError:
            print(f"薪资格式错误: {salary}")
            return None
    return f"{low}-{high}"

df['year_salary'] = df['salary'].apply(calculate_year_salary)

# 拆分'year_salary'列，并扩展为两个新列
df[['low_year_salary', 'high_year_salary']] = df['year_salary'].str.split('-', expand=True)

new_df = df[['id', 'company', 'year_salary', 'low_year_salary', 'high_year_salary']]

# 将更新后的DataFrame保存到新的CSV文件
new_df.to_csv('data/data_processed_salary.csv', index=False)
