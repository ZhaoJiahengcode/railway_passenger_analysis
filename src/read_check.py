import pandas as pd

# 读取刚刚生成的Excel文件
df = pd.read_excel('轨道交通客运量示例数据.xlsx')

# 查看数据前5行，确认是否成功读取
print(df.head())

# 查看数据基本信息
print("\n数据概况：")
print(df.info())

# 检查有没有缺失值
print("\n每列缺失值数量：")
print(df.isnull().sum())

git config --global user.name "ZhaoJiahengcode"
git config --global user.email "3520251616@qq.com"

