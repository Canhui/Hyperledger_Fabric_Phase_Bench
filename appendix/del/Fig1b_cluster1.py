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
x1_sub1 = ['209', '287', '337', '426', '524', '613', '725', '770']
measure_up_sub1 = [0.2852 + 0.0103, 0.4133 + 0.0145, 0.5848 + 0.0291, 0.7687 + 0.0741, 0.9044 + 0.0904, 1.0900 + 0.1982, 1.2347 + 0.2908, 1.1473 + 0.2199]
measure_low_sub1 = [0.2852 - 0.0103, 0.4133 - 0.0145, 0.5848 - 0.0291, 0.7687 - 0.0741, 0.9044 - 0.0904, 1.0900 - 0.1982, 1.2347 - 0.2908, 1.1473 - 0.2199]
model_our_sub1 = [0.3354, 0.4603, 0.5402, 0.6826, 0.8398, 0.9831, 1.1681, 1.281]
model_RefA_sub1 = [0.333, 0.4568, 0.5363, 0.6778, 0.8342, 0.9774, 1.167, 1.3201]
model_RefB_sub1 = [0.3343, 0.4586, 0.5382, 0.6804, 0.8371, 0.9802, 1.1676, 1.3005]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.fill_between(x, measure_up_sub1, measure_low_sub1, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 2])
ax1.text(0.00, 1.8,'cpu cores: 1')
ax1.tick_params(axis='both', which='major', labelsize=7)
ax1.annotate('Measurements', xy=(3.5, 0.95), xytext=(2, 1.5), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub2
x1_sub2 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
measure_up_sub2 = [0.2407 + 0.0173, 0.3333 + 0.0573, 0.4770 + 0.0928, 0.7355 + 0.1612, 0.7565 + 0.2216, 0.7848 + 0.2273, 0.8640 + 0.2406, 0.9509 + 0.1122]
measure_low_sub2 = [0.2407 - 0.0173, 0.3333 - 0.0573, 0.4770 - 0.0928, 0.7355 - 0.1612, 0.7565 - 0.2216, 0.7848 - 0.2273, 0.8640 - 0.2406, 0.9509 - 0.1122]
model_our_sub2 = [0.253, 0.3627, 0.5038, 0.6473, 0.7559, 0.7918, 0.8575, 0.8781]
model_RefA_sub2 = [0.2512, 0.361, 0.5015, 0.6447, 0.7534, 0.7896, 0.8571, 0.8793]
model_RefB_sub2 = [0.2515, 0.3613, 0.5018, 0.645, 0.7535, 0.7894, 0.856, 0.8774]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.fill_between(x, measure_up_sub2, measure_low_sub2, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 2])
ax2.text(0.00, 1.8,'cpu cores: 2')
ax2.tick_params(axis='both', which='major', labelsize=7)
ax2.annotate('Measurements', xy=(3.5, 0.95), xytext=(2, 1.5), color='#A9A9A9',
            xycoords='data',
            arrowprops=dict(color='#A9A9A9', shrink=0.001)
            )

# data sub3
x1_sub3 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
measure_up_sub3 = [0.1787 + 0.0143, 0.2175 + 0.0277, 0.3187 + 0.0323, 0.3406 + 0.0632, 0.3867 + 0.0748, 0.4386 + 0.1653, 0.4149 + 0.1778, 0.5322 + 0.2986]
measure_low_sub3 = [0.1787 - 0.0143, 0.2175 - 0.0277, 0.3187 - 0.0323, 0.3406 - 0.0632, 0.3867 - 0.0748, 0.4386 - 0.1653, 0.4149 - 0.1778, 0.5322 - 0.2986]
model_our_sub3 = [0.1445, 0.2073, 0.2876, 0.3693, 0.4308, 0.451, 0.4873, 0.498]
model_RefA_sub3 = [0.1444, 0.2073, 0.2876, 0.3693, 0.4309, 0.451, 0.4873, 0.4981]
model_RefB_sub3 = [0.1444, 0.2073, 0.2876, 0.3693, 0.4308, 0.451, 0.4874, 0.4981]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub3 = ax3.plot(x, model_RefB_sub3, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax3.fill_between(x, measure_up_sub3, measure_low_sub3, color =['#A9A9A9'], alpha=0.3) # color =['#7FFFAA'] color ref: https://blog.csdn.net/summerriver1/article/details/125215461
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 2])
ax3.text(0.00, 1.8,'cpu cores: 4')
ax3.tick_params(axis='both', which='major', labelsize=7)
ax3.annotate('Measurements', xy=(3.5, 0.5), xytext=(2, 1.05), color='#A9A9A9',
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

