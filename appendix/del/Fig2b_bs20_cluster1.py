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
measure_up_sub1 = [0.3817 + 0.1051, 0.4332 + 0.0792, 0.6884 + 0.1411]
measure_low_sub1 = [0.3817 - 0.1051, 0.4332 - 0.0792, 0.6884 - 0.1411]
model_our_sub1 = [0.3659, 0.4377, 0.7047]
model_RefA_sub1 = [0.2225, 0.3458, 0.6506]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 2])
ax1.text(0.00, 1.8,'OSNs: 3')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(1.8, 0.8), xytext=(0.9, 1.3), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax1.annotate('Waiting time', xy=(0.99, 0.40), xytext=(0.01, 0.9), color='#DC143C',
            xycoords='data',
            arrowprops=dict(color='#DC143C', shrink=0.001)
            )

# data sub2
x1_sub2 = ['70', '109', '180']
measure_up_sub2 = [0.4303 + 0.0636, 0.5279 + 0.1083, 0.9496 + 0.1345]
measure_low_sub2 = [0.4303 - 0.0636, 0.5279 - 0.1083, 0.9496 - 0.1345]
model_our_sub2 = [0.4319, 0.5404, 0.8744]
model_RefA_sub2 = [0.2886, 0.4486, 0.8204]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 2])
ax2.text(0.00, 1.8,'OSNs: 9')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(1.8, 1.0), xytext=(0.9, 1.5), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax2.annotate('Waiting time', xy=(0.99, 0.5), xytext=(0.01, 1), color='#DC143C',
            xycoords='data',
            arrowprops=dict(color='#DC143C', shrink=0.001)
            )

# data sub3
x1_sub3 = ['70', '109', '180']
measure_up_sub3 = [0.4199 + 0.0466, 0.4264 + 0.0589, 0.9091 + 0.1467]
measure_low_sub3 = [0.4199 - 0.0466, 0.4264 - 0.0589, 0.9091 - 0.1467]
model_our_sub3 = [0.3956, 0.484, 0.7811]
model_RefA_sub3 = [0.2522, 0.3921, 0.727]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 2])
ax3.text(0.00, 1.8,'OSNs: 15')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(1.8, 0.95), xytext=(0.9, 1.45), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax3.annotate('Waiting time', xy=(0.99, 0.45), xytext=(0.01, 0.9), color='#DC143C',
            xycoords='data',
            arrowprops=dict(color='#DC143C', shrink=0.001)
            )

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^r$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Overall latency $T^r$ (s)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1],     # The line objects
           labels = [r'Our model $T^r$', r'$M/M/1$ model $T^r$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

