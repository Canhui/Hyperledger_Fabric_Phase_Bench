import matplotlib.pyplot as plt 
import numpy as np

# plt.figure(figsize=(10,6))
# plt.plot(x,y)
# subfigs = fig.subfigures(1, 2, wspace=0.07)

# Set figures
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 2.2))
itp=0.07
gap=0.05
width=0.27
height=0.65
ax1.set_position([itp, 0.2, width, height])
ax2.set_position([itp+(width+gap)*1, 0.2, width, height])
ax3.set_position([itp+(width+gap)*2, 0.2, width, height])

# data sub1
x1_sub1 = ['209', '287', '337', '426', '524', '613', '725', '770']
y1_sub1 = [0.2837, 0.4116, 0.583, 0.7667, 0.9018, 1.0863, 1.225, 1.0966]
y2_sub1 = [0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013]
y3_sub1 = [0.0002, 0.0004, 0.0005, 0.0007, 0.0013, 0.0024, 0.0084, 0.0494]
x = np.arange(len(x1_sub1)) 
width = 0.25  # <----------------------------------adjust it ------------ 
line1_sub1 = ax1.bar(x - width*1, y1_sub1, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub1 = ax1.bar(x - width*0, y2_sub1, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub1 = ax1.bar(x + width*1, y3_sub1, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.set_yscale("log")
ax1.text(-0.4, 0.8,'cpu cores: 1')

# data sub2
x1_sub2 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
y1_sub2 = [0.2388, 0.3319, 0.4754, 0.7336, 0.7539, 0.7817, 0.8588, 0.944]
y2_sub2 = [0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013]
y3_sub2 = [0.0006, 0.0001, 0.0003, 0.0006, 0.0013, 0.0018, 0.0039, 0.0056]
x = np.arange(len(x1_sub2)) 
width = 0.25  # <----------------------------------adjust it ------------ 
line1_sub2 = ax2.bar(x - width*2, y1_sub2, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub2 = ax2.bar(x - width*1, y2_sub2, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub2 = ax2.bar(x + width*0, y3_sub2, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.set_yscale("log")
# ax2.text(width*4, 0.9,'2 cpu cores, cluster 1')
ax2.text(-0.7, 0.6,'cpu cores: 2')

# data sub3
x1_sub3 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
y1_sub3 = [0.1774, 0.2162, 0.3174, 0.3393, 0.3854, 0.4373, 0.4136, 0.5309]
y2_sub3 = [0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013, 0.0013]
y3_sub3 = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
x = np.arange(len(x1_sub3)) 
width = 0.25  # <----------------------------------adjust it ------------ 
line1_sub3 = ax3.bar(x - width*1, y1_sub3, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub3 = ax3.bar(x + width*0, y2_sub3, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub3 = ax3.bar(x + width*1, y3_sub3, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.set_yscale("log")
# ax3.text(width*4, 0.55,'4 cpu cores, cluster 1')
ax3.text(-0.5, 0.4,'cpu cores: 4')

# function to show the plot 
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^e$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Decomposed latencies (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line1_sub1, line2_sub1, line3_sub1],     # The line objects
           labels = [r'Measure $T_{comm}^e$', r'Measure $T_s^e$', r'Measure $T_q^e$'],
           ncol = 5,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 


