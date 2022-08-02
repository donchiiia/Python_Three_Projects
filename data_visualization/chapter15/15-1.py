import matplotlib.pyplot as plt


x_valus = list(range(1, 5001))
y_valus = [x ** 3 for x in x_valus]

plt.scatter(x_valus, y_valus, c=y_valus, cmap='Reds', s=1)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 设置标题和标签
plt.title("折线图（立方）", fontsize=24)
plt.xlabel("x轴", fontsize=14)
plt.ylabel("y轴", fontsize=14)

plt.show()
