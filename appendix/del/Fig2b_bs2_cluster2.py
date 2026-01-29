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
measure_up_sub1 = [0.0475 + 0.0041, 0.0548 + 0.0055, 0.0546 + 0.0034, 0.0707 + 0.0145, 0.0912 + 0.0208, 0.3738 + 0.1352]
measure_low_sub1 = [0.0475 - 0.0041, 0.0548 - 0.0055, 0.0546 - 0.0034, 0.0707 - 0.0145, 0.0912 - 0.0208, 0.3738 - 0.2352]
model_our_sub1 = [0.0411, 0.0502, 0.0558, 0.0659, 0.0871, 0.1220]
model_RefA_sub1 = [0.0368, 0.0469, 0.0528, 0.0635, 0.0852, 0.1209]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 0.8])
ax1.text(0.00, 0.72,'OSNs: 3')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(4.5, 0.35), xytext=(2.05, 0.55), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['244', '312', '352', '423', '566', '760']
measure_up_sub2 = [0.0505 + 0.0033, 0.0550 + 0.0061, 0.0569 + 0.0054, 0.0647 + 0.0073, 0.0765 + 0.0069, 0.0945 + 0.0279]
measure_low_sub2 = [0.0505 - 0.0033, 0.0550 - 0.0061, 0.0569 - 0.0054, 0.0647 - 0.0073, 0.0765 - 0.0069, 0.0945 - 0.0279]
model_our_sub2 = [0.0388, 0.0473, 0.0524, 0.0619, 0.0817, 0.1148]
model_RefA_sub2 = [0.0346, 0.044, 0.0496, 0.0596, 0.08, 0.1138]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 0.8])
ax2.text(0.00, 0.72,'OSNs: 9')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(4.5, 0.15), xytext=(2.05, 0.35), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub3
x1_sub3 = ['244', '312', '352', '423', '566', '760']
measure_up_sub3 = [0.0526 + 0.0032, 0.0588 + 0.0036, 0.0594 + 0.0066, 0.0580 + 0.0071, 0.0723 + 0.0120, 0.1580 + 0.0945]
measure_low_sub3 = [0.0526 - 0.0032, 0.0588 - 0.0036, 0.0594 - 0.0066, 0.0580 - 0.0071, 0.0723 - 0.0120, 0.1580 - 0.0945]
model_our_sub3 = [0.0409, 0.0499, 0.0554, 0.0655, 0.0866, 0.1213]
model_RefA_sub3 = [0.0366, 0.0466, 0.0526, 0.0632, 0.0848, 0.1203]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 0.8])
ax3.text(0.00, 0.72,'OSNs: 15')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(4.5, 0.19), xytext=(2.05, 0.39), color='#A9A9A9',
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

