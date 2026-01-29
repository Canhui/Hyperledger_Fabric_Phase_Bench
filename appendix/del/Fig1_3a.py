import matplotlib.pyplot as plt 
import numpy as np

# plt.figure(figsize=(10,6))
# plt.plot(x,y)
# subfigs = fig.subfigures(1, 2, wspace=0.07)

# Set figures
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.2))
itp=0.108
gap=0.08
width=0.39
height=0.65
ax1.set_position([itp, 0.2, width, height])
ax2.set_position([itp+(width+gap)*1, 0.2, width, height])

# data sub1
x1_sub1 = ['65', '82', '82', '82', '82', '82']
y1_sub1 = [2.4441/1024*100, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*10]
y2_sub1 = [2.4441/1024*100, 5.2920/1024*10, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*10]
y3_sub1 = [2.4441/1024*100, 6.2920/1024*100, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*900]
x = np.arange(len(x1_sub1)) 
width = 0.15  # <----------------------------------adjust it ------------ 
line1_sub1 = ax1.bar(x - width*1, y1_sub1, width, label='line1', color =['#0000CD'], hatch='+') # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub1 = ax1.bar(x - width*0, y2_sub1, width, label='line2', color =['#FF8C00'], hatch='\\') # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub1 = ax1.bar(x + width*1, y3_sub1, width, label='line3', color =['#008000'], hatch='//') # color =['#008000']
# line4_sub1 = ax1.bar(x + width*1, y4_sub1, width, label='line4', color =['#DC143C'], hatch='x') # color =['#DC143C']
# line5_sub1 = ax1.bar(x + width*2, y5_sub1, width, label='line5', color =['#8B008B'], hatch='--') # color =['#8B008B']
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_yscale("log")
ax1.text(width*12, 0.45,'3 OSNs')

# data sub2
x1_sub2 = ['65', '82', '82', '82', '82', '82']
y1_sub2 = [2.4441/1024*100, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*10]
y2_sub2 = [2.4441/1024*100, 5.2920/1024*10, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*20]
y3_sub2 = [2.4441/1024*100, 6.2920/1024*100, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*900]
# y4_sub2 = [2.4441/1024*100, 7.2920/1024*200, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90]
# y5_sub2 = [2.4441/1024*100, 4.2920/1024*400, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90, 4.2920/1024*90]
x = np.arange(len(x1_sub2)) 
width = 0.15  # <----------------------------------adjust it ------------ 
line1_sub2 = ax2.bar(x - width*1, y1_sub2, width, label='line1', color =['#0000CD'], hatch='+') # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub2 = ax2.bar(x - width*0, y2_sub2, width, label='line2', color =['#FF8C00'], hatch='\\') # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub2 = ax2.bar(x + width*1, y3_sub2, width, label='line3', color =['#008000'], hatch='//') # color =['#008000']
# line4_sub2 = ax2.bar(x + width*1, y4_sub2, width, label='line4', color =['#DC143C'], hatch='x') # color =['#DC143C']
# line5_sub2 = ax2.bar(x + width*2, y5_sub2, width, label='line5', color =['#8B008B'], hatch='--') # color =['#8B008B']
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_yscale("log")
ax2.text(width*12, 0.45,'3 OSNs')


# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^v$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Decomposed latencies (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line1_sub1, line2_sub1, line3_sub1],     # The line objects
           labels = [r'Measure $\beta^v$', r'Measure $\beta^v$', r'Measure $\beta^v$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 
