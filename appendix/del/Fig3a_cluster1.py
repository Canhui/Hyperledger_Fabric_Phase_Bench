import matplotlib.pyplot as plt 
import numpy as np

# Set figures
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.2))
itp=0.108
gap=0.08
width=0.39
height=0.65
ax1.set_position([itp, 0.2, width, height])
ax2.set_position([itp+(width+gap)*1, 0.2, width, height])

# data sub1
x1_sub1 = ['65', '82']
y1_sub1 = [0.6019, 0.5572] # T_{comm}
y2_sub1 = [0.0118, 0.0118] # T_s
y3_sub1 = [0.0224, 0.2993] # T_q
x = np.arange(len(x1_sub1)) 
width = 0.25  # <----------------------------------adjust it ------------ 
line1_sub1 = ax1.bar(x - width*1, y1_sub1, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub1 = ax1.bar(x - width*0, y2_sub1, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub1 = ax1.bar(x + width*1, y3_sub1, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.set_yscale("log")
ax1.text(-0.09, 0.5,'BS: 20')
#ax1.text(-0.09, 0.33,'Disk: HDD')

# data sub2
x1_sub2 = ['65', '109', '142']
y1_sub2 = [0.2220, 0.2573, 0.2408] # T_{comm}
y2_sub2 = [0.0054, 0.0054, 0.0054] # T_s
y3_sub2 = [0.0003, 0.0027, 0.0105] # T_q
x = np.arange(len(x1_sub2)) 
width = 0.25  # <----------------------------------adjust it ------------ 
line1_sub2 = ax2.bar(x - width*1, y1_sub2, width, label='line1', color =['#0000CD'], hatch='-', edgecolor='k', linewidth=0.5) # color =['#0000CD'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461 
line2_sub2 = ax2.bar(x - width*0, y2_sub2, width, label='line2', color =['#FF8C00'], hatch='\\', edgecolor='k', linewidth=0.5) # color =['#FF8C00'], hatch pattern https://blog.csdn.net/weixin_34613450/article/details/81744440
line3_sub2 = ax2.bar(x + width*1, y3_sub2, width, label='line3', color =['#8B008B'], hatch='//', edgecolor='k', linewidth=0.5) # color =['#008000']
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.set_yscale("log")
ax2.text(-0.09, 0.18,'BS: 50')
#ax2.text(-0.34, 0.10,'Disk: HDD')

# function to show the plot 
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^v$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Decomposed latencies (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line1_sub1, line2_sub1, line3_sub1],     # The line objects
           labels = [r'Measure $T_{comm}^v$', r'Measure $T_s^v$', r'Measure $T_q^v$'],
           ncol = 5,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 


