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
x1_sub1 = ['214', '244', '312', '352', '423', '460']
measure_up_sub1 = [0.2155 + 0.0128, 0.2478 + 0.0359, 0.3220 + 0.0241, 0.4218 + 0.0764, 0.5351 + 0.0772, 0.6225 + 0.0610]
measure_low_sub1 = [0.2155 - 0.0128, 0.2478 - 0.0359, 0.3220 - 0.0241, 0.4218 - 0.0764, 0.5351 - 0.0772, 0.6225 - 0.0610]
model_our_sub1 = [0.2388, 0.2721, 0.348, 0.3932, 0.4779, 0.5579]
model_RefA_sub1 = [0.235, 0.2678, 0.3432, 0.3885, 0.4779, 0.5967]
model_RefB_sub1 = [0.2369, 0.27, 0.3457, 0.391, 0.478, 0.5774]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 1])
ax1.text(0.00, 0.9,'cpu cores: 1')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(3.5, 0.55), xytext=(2, 0.8), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['244', '312', '352', '423', '460', '566', '670']
measure_up_sub2 = [0.0900 + 0.0036, 0.1074 + 0.0103, 0.1300 + 0.0125, 0.1686 + 0.0085, 0.1733 + 0.0180, 0.1935 + 0.0160, 0.2075 + 0.0136]
measure_low_sub2 = [0.0900 - 0.0036, 0.1074 - 0.0103, 0.1300 - 0.0125, 0.1686 - 0.0085, 0.1733 - 0.0180, 0.1935 - 0.0160, 0.2075 - 0.0136]
model_our_sub2 = [0.0876, 0.1115, 0.1255, 0.1505, 0.1636, 0.201, 0.238]
model_RefA_sub2 = [0.0875, 0.1114, 0.1255, 0.1504, 0.1635, 0.2011, 0.2384]
model_RefB_sub2 = [0.0876, 0.1114, 0.1255, 0.1505, 0.1635, 0.2011, 0.2382]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 1])
ax2.text(0.00, 0.9,'cpu cores: 2')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(3.5, 0.20), xytext=(2, 0.45), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub3
x1_sub3 = ['244', '312', '352', '423', '460', '566', '670']
measure_up_sub3 = [0.0706 + 0.0019, 0.0774 + 0.0045, 0.0788 + 0.0040, 0.0817 + 0.0038, 0.0943 + 0.0060, 0.1086 + 0.0030, 0.1163 + 0.0090]
measure_low_sub3 = [0.0706 - 0.0019, 0.0774 - 0.0045, 0.0788 - 0.0040, 0.0817 - 0.0038, 0.0943 - 0.0060, 0.1086 - 0.0030, 0.1163 - 0.0090]
model_our_sub3 = [0.0527, 0.0668, 0.075, 0.0898, 0.0974, 0.1194, 0.1409]
model_RefA_sub3 = [0.0526, 0.0668, 0.075, 0.0897, 0.0974, 0.1194, 0.141]
model_RefB_sub3 = [0.0526, 0.0667, 0.075, 0.0898, 0.0974, 0.1194, 0.141]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub3 = ax3.plot(x, model_RefB_sub3, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 1])
ax3.text(0.00, 0.9,'cpu cores: 4')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(3.5, 0.12), xytext=(2, 0.37), color='#A9A9A9',
            xycoords='data', 
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^e$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Overall latency $T^e$ (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1, line_model_RefB_sub1],     # The line objects
           labels = [r'Our model $T^e$', r'$M/M/1$ model $T^e$', r'$M/H_2/1$ model $T^e$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

