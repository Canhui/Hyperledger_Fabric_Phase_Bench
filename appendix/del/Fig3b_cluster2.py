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
x1_sub1 = ['78', '90', '150']
measure_up_sub1 = [0.0578 + 0.0086, 0.0518 + 0.0068, 0.2059 + 0.0220]
measure_low_sub1 = [0.0578 - 0.0086, 0.0518 - 0.0068, 0.2059 - 0.0820]
model_our_sub1 = [0.0601, 0.0690, 0.1283]
model_RefA_sub1 = [0.0595, 0.0685, 0.1289]
model_RefB_sub1 = [0.0600, 0.0689, 0.1249]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 0.5])
ax1.text(0.00, 0.45,'BS: 2')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(1.53, 0.15), xytext=(0.9, 0.30), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['78', '90', '150', '214', '240']
measure_up_sub2 = [0.0354 + 0.0100, 0.0362 + 0.0129, 0.0424 + 0.0085, 0.0538 + 0.0157, 0.0834 + 0.0099]
measure_low_sub2 = [0.0354 - 0.0100, 0.0362 - 0.0129, 0.0424 - 0.0085, 0.0538 - 0.0157, 0.0834 - 0.0099]
model_our_sub2 = [0.0262, 0.0301, 0.0497, 0.0706, 0.0791]
model_RefA_sub2 = [0.0262, 0.0301, 0.0496, 0.0706, 0.0791]
model_RefB_sub2 = [0.0262, 0.0301, 0.0497, 0.0706, 0.0791]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 0.5])
ax2.text(0.00, 0.45,'BS: 5')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(2.4, 0.09), xytext=(1.53, 0.24), color='#A9A9A9',
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

