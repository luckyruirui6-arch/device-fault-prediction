import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def 训练模型(数据文件, 特征列, 目标列, 模型保存路径):
    # 1. 读取数据
    数据 = pd.read_csv(数据文件)
    print(f"读取数据：{len(数据)}行")

    # 2. 特征和目标
    X = 数据[特征列]
    y = 数据[目标列]

    # 3. 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 4. 训练模型
    模型 = RandomForestClassifier()
    模型.fit(X_train, y_train)

    # 5. 评估
    y_pred = 模型.predict(X_test)
    准确率 = accuracy_score(y_test, y_pred)
    print(f"模型准确率：{准确率:.2%}")

    # 6. 保存模型
    joblib.dump(模型, 模型保存路径)
    print(f"模型已保存：{模型保存路径}")

    return 模型

def 预测(模型路径, 新数据):
    模型 = joblib.load(模型路径)
    预测结果 = 模型.predict(新数据)
    return 预测结果[0]

# 训练模型
模型 = 训练模型(
    数据文件="新设备数据_干净.csv",  # 改成新文件
    特征列=["温度", "压力", "运行时长"],  # 注意：这里有3个特征
    目标列="是否故障",
    模型保存路径="新故障预测模型.pkl"
)

# 测试预测
# 预测一个新设备
新设备 = [[87, 0.61, 150]]  # 温度87，压力0.61，运行时长150
结果 = 预测("新故障预测模型.pkl", 新设备)
print(f"温度87，压力0.61，运行时长150 → {'故障' if 结果 == 1 else '正常'}")