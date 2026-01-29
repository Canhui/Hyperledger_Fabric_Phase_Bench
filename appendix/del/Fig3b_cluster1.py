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
measure_up_sub1 = [0.6361 + 0.1358, 0.8683 + 0.1839]
measure_low_sub1 = [0.6361 - 0.1358, 0.8683 - 0.1839]
model_our_sub1 = [0.5437, 0.9538]
model_RefA_sub1 = [0.5475, 0.9611]
model_RefB_sub1 = [0.5768, 0.9296]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 2])
ax1.text(0.00, 1.8,'BS: 20')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(0.3, 0.9), xytext=(0.5, 1.4), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['65', '109', '142']
measure_up_sub2 = [0.2277 + 0.0415, 0.2654 + 0.0619, 0.2567 + 0.0403]
measure_low_sub2 = [0.2277 - 0.0415, 0.2654 - 0.0619, 0.2567 - 0.0403]
model_our_sub2 = [0.1550, 0.2585, 0.3421]
model_RefA_sub2 = [0.1542, 0.2578, 0.3420]
model_RefB_sub2 = [0.1552, 0.2587, 0.3413]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 2])
ax2.text(0.00, 1.8,'BS: 50')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(0.4, 0.35), xytext=(0.8, 0.8), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^e$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Overall latency $T^v$ (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1, line_model_RefB_sub1],     # The line objects
           labels = [r'Our model $T^v$', r'$M/M/1$ model $T^v$', r'$M/E_r/1$ model $T^v$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

