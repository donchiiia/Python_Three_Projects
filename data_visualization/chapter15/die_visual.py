from die import Die
import pygal

# 创建两个骰子
die_1 = Die(6)
die_2 = Die(10)

# 掷几次骰子，将结果存放在一个列表中
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = 'Results of rolling a D6 and a D10 1,000,000 times.'
hist.x_labels = []
for i in range(2, max_result + 1):
    hist.x_labels.append(str(i))
print(hist.x_labels)
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

