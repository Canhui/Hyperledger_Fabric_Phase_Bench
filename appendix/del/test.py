import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] # 解决中文乱码

labels = ['第一项', '第二项']
a = [4.0, 3.8]
b = [26.9, 48.1]
c = [55.6, 63.0]
d = [59.3, 81.5]
e = [89, 90]    


x = np.arange(len(labels))  # 标签位置
width = 0.1  # 柱状图的宽度，可以根据自己的需求和审美来改

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*2, a, width, label='a')
rects2 = ax.bar(x - width+0.01, b, width, label='b')
rects3 = ax.bar(x + 0.02, c, width, label='c')
rects4 = ax.bar(x + width+ 0.03, d, width, label='d')
rects5 = ax.bar(x + width*2 + 0.04, e, width, label='e')


# 为y轴、标题和x轴等添加一些文本。
ax.set_ylabel('Y轴', fontsize=16)
ax.set_xlabel('X轴', fontsize=16)
ax.set_title('这里是标题')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


# def autolabel(rects):
#     """在*rects*中的每个柱状条上方附加一个文本标签，显示其高度"""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3点垂直偏移
#                     textcoords="offset points",
#                     ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
# autolabel(rects4)
# autolabel(rects5)

# fig.tight_layout()

plt.show()
