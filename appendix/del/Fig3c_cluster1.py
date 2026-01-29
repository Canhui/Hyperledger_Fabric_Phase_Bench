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
model_our_sub1 = [2.5310/1024*100, 3.4492/1024*100]
model_RefA_sub1 = [2.5310/1024*100, 3.5930/1024*100]
model_RefB_sub1 = [2.5578/1024*100, 3.1235/1024*100]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 3])
ax1.text(0.00, 2.7,'BS: 20')
ax1.text(0.00, 2.4,'Ethernet network: 1Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['65', '109', '142']
model_our_sub2 = [6.8623/1024*100, 9.9288/1024*100, 13.8211/1024*100]
model_RefA_sub2 = [6.9437/1024*100, 10.1296/1024*100, 14.2593/1024*100]
model_RefB_sub2 = [6.9216/1024*100, 10.0499/1024*100, 13.9896/1024*100]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 3])
ax2.text(0.00, 2.7,'BS: 50')
ax2.text(0.00, 2.4,'Ethernet network: 1Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^v$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Bandwidth utility (%)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1, line_model_RefB_sub1],     # The line objects
           labels = [r'Our model $\beta^v$', r'$M/M/1$ model $\beta^v$', r'$M/H_2/1$ model $\beta^v$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

