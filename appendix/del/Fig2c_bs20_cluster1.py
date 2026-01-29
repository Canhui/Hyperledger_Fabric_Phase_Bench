import matplotlib.pyplot as plt 
import numpy as np

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
model_our_p1_sub1 = [40.7103/1024*100, 49.0343/1024*100, 75.7406/1024*100]
model_our_p2_sub1 = [17.0189/1024*100, 18.1312/1024*100, 17.3326/1024*100]
model_RefA_p1_sub1 = [40.7103/1024*100, 49.0343/1024*100, 75.7406/1024*100]
model_RefA_p2_sub1 = [17.2607/1024*100, 18.4454/1024*100, 17.685/1024*100]
x = np.arange(len(x1_sub1)) 
line_model_our_p1_sub1 = ax1.plot(x, model_our_p1_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub1 = ax1.plot(x, model_our_p2_sub1, color='#000000', linestyle='dashed', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub1 = ax1.plot(x, model_RefA_p1_sub1, color='#CD853F', linestyle='solid', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub1 = ax1.plot(x, model_RefA_p2_sub1, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 30])
ax1.text(0.00, 27,'OSNs: 3')
ax1.text(0.00, 24,'Ethernet network: 1Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['70', '109', '180']
model_our_p1_sub2 = [38.8774/1024*100, 54.8216/1024*100, 101.1691/1024*100]
model_our_p2_sub2 = [54.8017/1024*100, 53.5013/1024*100, 44.2913/1024*100]
model_RefA_p1_sub2 = [38.8774/1024*100, 54.8216/1024*100, 101.1691/1024*100]
model_RefA_p2_sub2 = [55.4265/1024*100, 54.1821/1024*100, 44.8624/1024*100]
x = np.arange(len(x1_sub2)) 
line_model_our_p1_sub2 = ax2.plot(x, model_our_p1_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub2 = ax2.plot(x, model_our_p2_sub2, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub2 = ax2.plot(x, model_RefA_p1_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub2 = ax2.plot(x, model_RefA_p2_sub2, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 30])
ax2.text(0.00, 27,'OSNs: 9')
ax2.text(0.00, 24,'Ethernet network: 1Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['70', '109', '180']
model_our_p1_sub3 = [31.4296/1024*100, 46.5335/1024*100, 79.2998/1024*100]
model_our_p2_sub3 = [104.8323/1024*100, 131.3947/1024*100, 83.1866/1024*100]
model_RefA_p1_sub3 = [31.4296/1024*100, 46.5335/1024*100, 79.2998/1024*100]
model_RefA_p2_sub3 = [106.1402/1024*100, 133.7533/1024*100, 84.3389/1024*100]
x = np.arange(len(x1_sub3)) 
line_model_our_p1_sub3 = ax3.plot(x, model_our_p1_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub3 = ax3.plot(x, model_our_p2_sub3, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub3 = ax3.plot(x, model_RefA_p1_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub3 = ax3.plot(x, model_RefA_p2_sub3, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 30])
ax3.text(0.00, 27,'OSNs: 15')
ax3.text(0.00, 24,'Ethernet network: 1Gbps')
ax3.tick_params(axis='both', which='major', labelsize=7)

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^r$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Bandwidth utility (%)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_p1_sub1, line_model_our_p2_sub1, line_model_RefA_p1_sub1, line_model_RefA_p2_sub1],     # The line objects
           labels = [r'Our model $\beta_{c2l}^r$', r'Our model $\beta_{l2f}^r$', r'$M/M/1$ model $\beta_{c2l}^r$', r'$M/M/1$ model $\beta_{l2f}^r$'],
           ncol = 4,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

