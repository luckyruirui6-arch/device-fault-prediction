import pandas as pd

def 清洗数据(输入文件, 输出文件):
    """
    读取CSV，用中位数填充缺失的温度，保存到新文件
    """
    # 读取数据
    数据 = pd.read_csv(输入文件)
    
    # 打印原始缺失情况
    print(f"原始数据：{len(数据)}行")
    print(f"温度缺失数量：{数据['温度'].isnull().sum()}")
    
    # 用中位数填充温度
    数据["温度"] = 数据["温度"].fillna(数据["温度"].mode())
    
    # 保存到新文件
    数据.to_csv(输出文件, index=False)
    print(f"清洗完成，保存到：{输出文件}")
    print(f"清洗后数据：{len(数据)}行")
    
    return 数据

# 使用函数
if __name__ == "__main__":
    干净数据 = 清洗数据("新设备数据.csv", "新设备数据_干净.csv")
    print("\n前5行预览：")
    print(干净数据.head())