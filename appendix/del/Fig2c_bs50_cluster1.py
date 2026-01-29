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
x1_sub1 = ['109', '180', '263', '310', '342']
model_our_p1_sub1 = [49.5094/1024*100, 76.4266/1024*100, 114.3611/1024*100, 171.3591/1024*100, 174.6324/1024*100]
model_our_p2_sub1 = [51.7667/1024*100, 51.1984/1024*100, 63.9094/1024*100, 45.985/1024*100, 51.9652/1024*100]
model_RefA_p1_sub1 = [49.5094/1024*100, 76.4266/1024*100, 114.3611/1024*100, 171.3591/1024*100, 174.6324/1024*100]
model_RefA_p2_sub1 = [52.3502/1024*100, 51.8274/1024*100, 64.9875/1024*100, 46.6044/1024*100, 52.7865/1024*100]
x = np.arange(len(x1_sub1)) 
line_model_our_p1_sub1 = ax1.plot(x, model_our_p1_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub1 = ax1.plot(x, model_our_p2_sub1, color='#000000', linestyle='dashed', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub1 = ax1.plot(x, model_RefA_p1_sub1, color='#CD853F', linestyle='solid', marker='*',  markersize=8, linewidth=2.0)
line_model_RefA_p2_sub1 = ax1.plot(x, model_RefA_p2_sub1, color='#CD853F', linestyle='dashed', marker='x',  markersize=8, linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 50])
ax1.text(0.00, 45,'OSNs: 3')
ax1.text(0.00, 40,'Ethernet network: 1Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['109', '180', '263', '310', '342']
model_our_p1_sub2 = [46.2806/1024*100, 72.2389/1024*100, 108.3315/1024*100, 164.0096/1024*100, 173.1237/1024*100]
model_our_p2_sub2 = [147.5632/1024*100, 196.3351/1024*100, 190.5429/1024*100, 180.5685/1024*100, 191.1896/1024*100]
model_RefA_p1_sub2 = [46.2806/1024*100, 72.2389/1024*100, 108.3315/1024*100, 164.0096/1024*100, 173.1237/1024*100]
model_RefA_p2_sub2 = [148.7445/1024*100, 198.6463/1024*100, 192.9284/1024*100, 182.9556/1024*100, 193.9655/1024*100]
x = np.arange(len(x1_sub2)) 
line_model_our_p1_sub2 = ax2.plot(x, model_our_p1_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub2 = ax2.plot(x, model_our_p2_sub2, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub2 = ax2.plot(x, model_RefA_p1_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefA_p2_sub2 = ax2.plot(x, model_RefA_p2_sub2, color='#CD853F', linestyle='dashed', marker='x', markersize=8, linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 50])
ax2.text(0.00, 45,'OSNs: 9')
ax2.text(0.00, 40,'Ethernet network: 1Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['109', '180', '263', '310', '342']
model_our_p1_sub3 = [64.3498/1024*100, 96.0991/1024*100, 169.8089/1024*100, 177.2104/1024*100, 214.8961/1024*100]
model_our_p2_sub3 = [236.5451/1024*100, 302.11/1024*100, 360.4715/1024*100, 298.383/1024*100, 342.9668/1024*100]
model_RefA_p1_sub3 = [64.3498/1024*100, 96.0991/1024*100, 169.8089/1024*100, 177.2104/1024*100, 214.8961/1024*100]
model_RefA_p2_sub3 = [238.2786/1024*100, 305.2326/1024*100, 365.3551/1024*100, 302.105/1024*100, 348.073/1024*100]
x = np.arange(len(x1_sub3)) 
line_model_our_p1_sub3 = ax3.plot(x, model_our_p1_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub3 = ax3.plot(x, model_our_p2_sub3, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub3 = ax3.plot(x, model_RefA_p1_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefA_p2_sub3 = ax3.plot(x, model_RefA_p2_sub3, color='#CD853F', linestyle='dashed', marker='x', markersize=8, linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 50])
ax3.text(0.00, 45,'OSNs: 15')
ax3.text(0.00, 40,'Ethernet network: 1Gbps')
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

