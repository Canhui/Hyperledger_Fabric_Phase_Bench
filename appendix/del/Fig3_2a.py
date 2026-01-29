import matplotlib.pyplot as plt 
import numpy as np

# plt.figure(figsize=(10,6))
# plt.plot(x,y)
# subfigs = fig.subfigures(1, 2, wspace=0.07)

# Set figures
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 2.2))
itp=0.08
gap=0.07
width=0.25
height=0.65
ax1.set_position([itp, 0.2, width, height])
ax2.set_position([itp+(width+gap)*1, 0.2, width, height])
ax3.set_position([itp+(width+gap)*2, 0.2, width, height])

# data sub1
x1_sub1 = ['65', '82', '82']
measure_up_sub1 = [2.4441/1024*100+0.1, 2.2920/1024*100+0.1, 2.2920/1024*100+0.1]
measure_low_sub1 = [2.4441/1024*100-0.1, 2.2920/1024*100-0.1, 2.2920/1024*100-0.1]
model_our_sub1 = [2.4441/1024*100, 2.2920/1024*100, 2.2920/1024*100]
model_RefA_sub1 = [2.4441/1024*100+0.5, 2.2920/1024*100+0.5, 2.2920/1024*100+0.5]
model_RefB_sub1 = [2.4441/1024*100+0.4, 2.2920/1024*100+0.4, 2.2920/1024*100+0.4]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*',  linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.',  linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 1])
ax1.text(width*2.8, 0.9, '3 OSNs')

# data sub2
x1_sub2 = ['65', '82', '82']
measure_up_sub2 = [2.4441/1024*100+0.1, 2.2920/1024*100+0.1, 2.2920/1024*100+0.1]
measure_low_sub2 = [2.4441/1024*100-0.1, 2.2920/1024*100-0.1, 2.2920/1024*100-0.1]
model_our_sub2 = [2.4441/1024*100, 2.2920/1024*100, 2.2920/1024*100]
model_RefA_sub2 = [2.4441/1024*100+0.5, 2.2920/1024*100+0.5, 2.2920/1024*100+0.5]
model_RefB_sub2 = [2.4441/1024*100+0.4, 2.2920/1024*100+0.4, 2.2920/1024*100+0.4]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*',  linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.',  linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 1])
ax2.text(width*2.8, 0.9, '9 OSNs')

# data sub3
x1_sub3 = ['65', '82', '82']
measure_up_sub3 = [2.4441/1024*100+0.1, 2.2920/1024*100+0.1, 2.2920/1024*100+0.1]
measure_low_sub3 = [2.4441/1024*100-0.1, 2.2920/1024*100-0.1, 2.2920/1024*100-0.1]
model_our_sub3 = [2.4441/1024*100, 2.2920/1024*100, 2.2920/1024*100]
model_RefA_sub3 = [2.4441/1024*100+0.5, 2.2920/1024*100+0.5, 2.2920/1024*100+0.5]
model_RefB_sub3 = [2.4441/1024*100+0.4, 2.2920/1024*100+0.4, 2.2920/1024*100+0.4]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*',  linewidth=2.0)
line_model_RefB_sub3 = ax3.plot(x, model_RefB_sub3, color='#00BFFF', linestyle='dashed', marker='.',  linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 1])
ax3.text(width*2.8, 0.9, '15 OSNs')

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^v$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Bandwidth utility (%)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1, line_model_RefB_sub1],     # The line objects
           labels = [r'Our model', r'Ref1 model', r'Ref2 model'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 
