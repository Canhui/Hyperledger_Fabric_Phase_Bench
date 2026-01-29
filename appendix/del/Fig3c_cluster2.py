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
model_our_sub1 = [35.4976/10240*100, 47.0843/10240*100, 19.4233/10240*100]
model_RefA_sub1 = [38.0859/10240*100, 51.955/10240*100, 20.3804/10240*100]
model_RefB_sub1 = [37.3087/10240*100, 50.2232/10240*100, 19.5857/10240*100]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 3])
ax1.text(0.00, 2.7,'BS: 2')
ax1.text(0.00, 2.4,'Ethernet network: 10Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['78', '90', '150', '214', '240']
model_our_sub2 = [52.6837/10240*100, 59.419/10240*100, 84.3076/10240*100, 94.4562/10240*100, 68.0169/10240*100]
model_RefA_sub2 = [52.6837/10240*100, 59.419/10240*100, 84.3076/10240*100, 94.6344/10240*100, 68.0993/10240*100]
model_RefB_sub2 = [52.6837/10240*100, 59.419/10240*100, 84.3076/10240*100, 94.4562/10240*100, 68.0169/10240*100]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 3])
ax2.text(0.00, 2.7,'BS: 5')
ax2.text(0.00, 2.4,'Ethernet network: 10Gbps')
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

