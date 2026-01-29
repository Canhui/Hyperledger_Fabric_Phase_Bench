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
x1_sub1 = ['109', '180', '263', '310', '342']
measure_up_sub1 = [0.3824 + 0.0481, 0.3622 + 0.0346, 0.3480 + 0.0473, 0.4515 + 0.1325, 0.4584 + 0.1088]
measure_low_sub1 = [0.3824 - 0.0481, 0.3622 - 0.0346, 0.3480 - 0.0473, 0.4515 - 0.1325, 0.4584 - 0.1088]
model_our_sub1 = [0.3504, 0.3375, 0.3865, 0.4294, 0.475]
model_RefA_sub1 = [0.1207, 0.1984, 0.2914, 0.3492, 0.4025]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 2])
ax1.text(0.00, 1.8,'OSNs: 3')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(3.0, 0.6), xytext=(2.2, 1.1), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax1.annotate('Waiting time', xy=(0.15, 0.25), xytext=(0.7, 0.8), color='#DC143C',
            xycoords='data',
            arrowprops=dict(color='#DC143C', shrink=0.001)
            )

# data sub2
x1_sub2 = ['109', '180', '263', '310', '342']
measure_up_sub2 = [0.4258 + 0.0666, 0.3725 + 0.0433, 0.4169 + 0.0367, 0.4593 + 0.0660, 0.4857 + 0.1046]
measure_low_sub2 = [0.4258 - 0.0666, 0.3725 - 0.0433, 0.4169 - 0.0367, 0.4593 - 0.0660, 0.4857 - 0.1046]
model_our_sub2 = [0.3675, 0.3658, 0.4279, 0.4782, 0.5289]
model_RefA_sub2 = [0.1379, 0.2267, 0.3328, 0.3980, 0.4563]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 2])
ax2.text(0.00, 1.8,'OSNs: 9')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(3.0, 0.6), xytext=(2.2, 1.1), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax2.annotate('Waiting time', xy=(0.15, 0.25), xytext=(0.7, 0.8), color='#DC143C',
            xycoords='data',
            arrowprops=dict(color='#DC143C', shrink=0.001)
            )

# data sub3
x1_sub3 = ['109', '180', '263', '310', '342']
measure_up_sub3 = [0.4230 + 0.0281, 0.3816 + 0.0154, 0.3769 + 0.0294, 0.4750 + 0.0480, 0.4685 + 0.0711]
measure_low_sub3 = [0.4230 - 0.0281, 0.3816 - 0.0154, 0.3769 - 0.0294, 0.4750 - 0.0480, 0.4685 - 0.0711]
model_our_sub3 = [0.3659, 0.3631, 0.4240, 0.4735, 0.5237]
model_RefA_sub3 = [0.1362, 0.2239, 0.3287, 0.3932, 0.4511]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 2])
ax3.text(0.00, 1.8,'OSNs: 15')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(3.0, 0.6), xytext=(2.2, 1.1), color='#A9A9A9',
            xycoords='data', 
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )
ax3.annotate('Waiting time', xy=(0.15, 0.25), xytext=(0.7, 0.8), color='#DC143C',
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

