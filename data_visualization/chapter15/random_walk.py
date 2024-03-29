from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, start, end):
        direction = choice([1, -1])
        distance = choice([x for x in range(start, end)])
        step = distance * direction
        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直至列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着这个方向前进的距离
            # x_direction = choice([1, -1])
            # x_distance = choice([x for x in range(0, 5)])
            # x_step = x_distance * x_direction
            #
            # y_direction = choice([1, -1])
            # y_distance = choice([y for y in range(0, 5)])
            # y_step = y_distance * y_direction

            # 拒绝原地踏步
            x_step = self.get_step(0, 8)
            y_step = self.get_step(0, 8)
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)