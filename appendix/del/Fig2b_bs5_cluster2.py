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
x1_sub1 = ['244', '312', '352', '423', '566', '760']
measure_up_sub1 = [0.0450 + 0.0069, 0.0445 + 0.0045, 0.0487 + 0.0053, 0.0489 + 0.0077, 0.0470 + 0.0082, 0.0488 + 0.0076]
measure_low_sub1 = [0.0450 - 0.0069, 0.0445 - 0.0045, 0.0487 - 0.0053, 0.0489 - 0.0077, 0.0470 - 0.0082, 0.0488 - 0.0076]
model_our_sub1 = [0.0328, 0.0367, 0.0393, 0.0445, 0.0558, 0.0722]
model_RefA_sub1 = [0.0225, 0.0286, 0.0322, 0.0386, 0.0515, 0.0690]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 0.5])
ax1.text(0.00, 0.44,'OSNs: 3')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(4.5, 0.08), xytext=(2.05, 0.22), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['244', '312', '352', '423', '566', '760']
measure_up_sub2 = [0.0476 + 0.0059, 0.0519 + 0.0060, 0.0548 + 0.0070, 0.0508 + 0.0074, 0.0556 + 0.0051, 0.0538 + 0.0058]
measure_low_sub2 = [0.0476 - 0.0059, 0.0519 - 0.0060, 0.0548 - 0.0070, 0.0508 - 0.0074, 0.0556 - 0.0051, 0.0538 - 0.0058]
model_our_sub2 = [0.0354, 0.0400, 0.0431, 0.0490, 0.0619, 0.0803]
model_RefA_sub2 = [0.0251, 0.0319, 0.0360, 0.0431, 0.0576, 0.0771]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 0.5])
ax2.text(0.00, 0.44,'OSNs: 9')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(4.5, 0.08), xytext=(2.05, 0.22), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub3
x1_sub3 = ['244', '312', '352', '423', '566', '760']
measure_up_sub3 = [0.0463 + 0.0045, 0.0478 + 0.0033, 0.0525 + 0.0022, 0.0480 + 0.0064, 0.0507 + 0.0077, 0.0490 + 0.0096]
measure_low_sub3 = [0.0463 - 0.0045, 0.0478 - 0.0033, 0.0525 - 0.0022, 0.0480 - 0.0064, 0.0507 - 0.0077, 0.0490 - 0.0096]
model_our_sub3 = [0.0337, 0.0378, 0.0407, 0.0461, 0.0579, 0.0750]
model_RefA_sub3 = [0.0234, 0.0297, 0.0335, 0.0403, 0.0536, 0.0718]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 0.5])
ax3.text(0.00, 0.44,'OSNs: 15')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(4.5, 0.08), xytext=(2.05, 0.22), color='#A9A9A9',
            xycoords='data', 
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
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

