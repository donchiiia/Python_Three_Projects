import matplotlib.pyplot as plt


x_values = list(range(1, 1100))
y_values = [x ** 2 for x in x_values]
# 参数c=颜色，就显示那种颜色，c=一个值列表，cmap确定使用哪种颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='none', s=40)

plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis="both", which='major', labelsize=14)

# 要想程序自动保存图片至文件，可使用plt.savefig()代替plt.show()
# savefig()第一个参数是指定保存文件的文件名，第二个参数是指定是否对图片边缘进行裁剪
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
