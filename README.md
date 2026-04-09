# 设备故障预测系统

## 项目简介
基于随机森林算法的设备故障预测系统。输入设备温度、压力、运行时长，输出故障预测结果。

## 技术栈
- Python 3.13
- Pandas
- Scikit-learn
- Joblib

## 项目文件
- `data_cleaner.py` - 数据清洗
- `fault_model.py` - 模型训练和预测
- `predict_app.py` - 交互式预测

## 使用方法
1. 运行 fault_model.py 训练模型
2. 运行 predict_app.py 输入参数预测
