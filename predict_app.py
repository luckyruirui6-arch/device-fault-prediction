import joblib

# 加载保存好的模型
模型 = joblib.load("故障预测模型.pkl")

print("=" * 40)
print("设备故障预测系统")
print("=" * 40)

# 让用户输入数据
温度 = float(input("请输入温度："))
压力 = float(input("请输入压力："))

# 准备预测数据
新设备 = [[温度, 压力]]

# 预测
预测结果 = 模型.predict(新设备)

print("\n" + "=" * 40)
if 预测结果[0] == 1:
    print("⚠️ 预测结果：设备会故障")
    print("建议：立即检查设备")
else:
    print("✅ 预测结果：设备正常")
    print("建议：继续监控")
print("=" * 40)