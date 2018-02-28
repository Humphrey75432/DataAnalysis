# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt

# 横坐标数值
input_values = [1,2,3,4,5];

# 纵坐标数值
squares = [1,4,9,16,25];

# 绘制图表
plt.plot(input_values, squares, lineWidth=5)

# 设置标题
plt.title("Square Numbers", fontsize=24)

# 设置横轴标签
plt.xlabel("Value", fontsize=14)

# 设置纵轴标签
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

# 显示图表
plt.show()