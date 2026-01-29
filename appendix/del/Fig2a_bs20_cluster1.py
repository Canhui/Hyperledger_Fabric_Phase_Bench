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
x1_sub1 = ['70', '109', '180']
y1_sub1 = [0.0403, 0.0521, 0.0557] # T_{c2l}^r
y2_sub1 = [0.0053, 0.0053, 0.0053] # T_{s}^r
y3_sub1 = [0.0004, 0.0023, 0.085] # T_{q}^r
y4_sub1 = [0.1429, 0.0917, 0.0556] # T_{w}^r
y5_sub1 = [0.1928, 0.2818, 0.4868] # T_{l2f}^r
x = np.arange(len(x1_sub1)) 
width = 0.14  # <----------------------------------adjust it ------------ 
line1_sub1 = ax1.bar(x - width*2, y1_sub1, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub1 = ax1.bar(x - width*1, y2_sub1, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub1 = ax1.bar(x + width*0, y3_sub1, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
line4_sub1 = ax1.bar(x + width*1, y4_sub1, width, label='line4', color =['#DC143C'], hatch='x', edgecolor='k', linewidth=0.5) # color =['#DC143C']
line5_sub1 = ax1.bar(x + width*2, y5_sub1, width, label='line5', color =['#008000'], hatch='.', edgecolor='k', linewidth=0.5) # color =['#8B008B']
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.set_yscale("log")
ax1.text(-0.4, 0.35,'OSNs: 3')

# data sub2
x1_sub2 = ['70', '109', '180']
y1_sub2 = [0.0422, 0.0466, 0.0417] # T_{c2l}^r
y2_sub2 = [0.0053, 0.0053, 0.0053] # T_{s}^r
y3_sub2 = [0.0004, 0.0023, 0.085] # T_{q}^r
y4_sub1 = [0.1429, 0.0917, 0.0556] # T_{w}^r
y5_sub1 = [0.2395, 0.382, 0.762] # T_{l2f}^r
x = np.arange(len(x1_sub2)) 
width = 0.14  # <----------------------------------adjust it ------------ 
line1_sub2 = ax2.bar(x - width*2, y1_sub2, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub2 = ax2.bar(x - width*1, y2_sub2, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub2 = ax2.bar(x + width*0, y3_sub2, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
line4_sub2 = ax2.bar(x + width*1, y4_sub1, width, label='line4', color =['#DC143C'], hatch='x', edgecolor='k', linewidth=0.5) # color =['#DC143C']
line5_sub2 = ax2.bar(x + width*2, y5_sub1, width, label='line5', color =['#008000'], hatch='.', edgecolor='k', linewidth=0.5) # color =['#8B008B']
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.set_yscale("log")
# ax2.text(width*4, 0.9,'2 cpu cores, cluster 1')
ax2.text(-0.4, 0.5,'OSNs: 9')

# data sub3
x1_sub3 = ['70', '109', '180']
y1_sub3 = [0.0522, 0.0549, 0.0532] # T_{c2l}^r
y2_sub3 = [0.0053, 0.0053, 0.0053] # T_{s}^r
y3_sub3 = [0.0004, 0.0023, 0.085] # T_{q}^r
y4_sub1 = [0.1429, 0.0917, 0.0556] # T_{w}^r
y5_sub1 = [0.2191, 0.2722, 0.71] # T_{l2f}^r
x = np.arange(len(x1_sub3)) 
width = 0.14  # <----------------------------------adjust it ------------ 
line1_sub3 = ax3.bar(x - width*2, y1_sub3, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub3 = ax3.bar(x - width*1, y2_sub3, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub3 = ax3.bar(x + width*0, y3_sub3, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
line4_sub3 = ax3.bar(x + width*1, y4_sub1, width, label='line4', color =['#DC143C'], hatch='x', edgecolor='k', linewidth=0.5) # color =['#DC143C']
line5_sub3 = ax3.bar(x + width*2, y5_sub1, width, label='line5', color =['#008000'], hatch='.', edgecolor='k', linewidth=0.5) # color =['#8B008B']
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.set_yscale("log")
# ax3.text(width*4, 0.55,'4 cpu cores, cluster 1')
ax3.text(-0.4, 0.5,'OSNs: 15')

# function to show the plot 
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^r$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Decomposed latencies (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line1_sub1, line2_sub1, line3_sub1, line4_sub1, line5_sub1],     # The line objects
           labels = [r'Measure $T_{c2l}^r$', r'Measure $T_{s}^r$', r'Measure $T_{q}^r$', r'Measure $T_{w}^r$', r'Measure $T_{l2f}^r$'],
           ncol = 5,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 


