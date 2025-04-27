import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    """加载数据，如果文件不存在则给出提示"""
    if not os.path.exists(filepath):
        print(f"❌ 文件不存在: {filepath}")
        return None
    try:
        df = pd.read_excel(filepath)
        print(f"✅ 成功加载数据！共有 {df.shape[0]} 条记录，{df.shape[1]} 个字段。")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ 读取数据时出错：{e}")
        return None

def plot_passenger_trend(df):
    """绘制各城市客运量趋势图"""
    if df is None or df.empty:
        print("❌ 数据为空，无法绘图。")
        return

    # 配置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    cities = df['城市'].unique()
    plt.figure(figsize=(10, 6))

    for city in cities:
        city_data = df[df['城市'] == city]
        plt.plot(city_data['月份'], city_data['客运量（万人次）'], marker='o', label=city)

    plt.title('各城市客运量趋势')
    plt.xlabel('月份')
    plt.ylabel('客运量（万人次）')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    filepath = '轨道交通客运量示例数据.xlsx'  # 文件路径
    df = load_data(filepath)
    plot_passenger_trend(df)

if __name__ == "__main__":
    main()
