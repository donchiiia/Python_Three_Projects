import matplotlib.pyplot as plt

input_value = list(range(1, 6))
squares = [x ** 2 for x in input_value]
plt.plot(input_value, squares, linewidth=3)

# 设置图标标题，并为坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=10)

plt.show()
