import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于运行的状态，就不停的执行模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其所包含的所有点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(8, 6))
    # 隐藏坐标轴
    axes = plt.axes()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    # 隐藏坐标轴后隐藏图像的边框
    plt.axis('off')

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
    # 突出起点和终点
    plt.scatter(0, 0, edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input("Make another walk?(y/n)\n")
    if keep_running == 'n':
        break
