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
x1_sub1 = ['244', '312', '352', '423', '566', '760']
model_our_p1_sub1 = [227.8386/10240*100, 329.3919/10240*100, 378.4404/10240*100, 238.8931/10240*100, 594.8711/10240*100, 795.2009/10240*100]
model_our_p2_sub1 = [668.8596/10240*100, 518.617/10240*100, 574.9129/10240*100, 780.6348/10240*100, 408.802/10240*100, 104.4721/10240*100]
model_RefA_p1_sub1 = [227.8386/10240*100, 329.3919/10240*100, 378.4404/10240*100, 238.8931/10240*100, 594.8711/10240*100, 795.2009/10240*100]
model_RefA_p2_sub1 = [684.8802/10240*100, 529.8913/10240*100, 589.2857/10240*100, 812.6281/10240*100, 417.158/10240*100, 105.0885/10240*100]
x = np.arange(len(x1_sub1)) 
line_model_our_p1_sub1 = ax1.plot(x, model_our_p1_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub1 = ax1.plot(x, model_our_p2_sub1, color='#000000', linestyle='dashed', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub1 = ax1.plot(x, model_RefA_p1_sub1, color='#CD853F', linestyle='solid', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub1 = ax1.plot(x, model_RefA_p2_sub1, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 70])
ax1.text(0.00, 62,'OSNs: 3')
ax1.text(0.00, 56,'Ethernet network: 10Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['244', '312', '352', '423', '566', '760']
model_our_p1_sub2 = [242.3199/10240*100, 341.7056/10240*100, 323.5294/10240*100, 440.625/10240*100, 611.3191/10240*100, 813.3562/10240*100]
model_our_p2_sub2 = [2118.0556/10240*100, 2003.4247/10240*100, 2417.5824/10240*100, 2065.4297/10240*100, 2089.0748/10240*100, 2290.9968/10240*100]
model_RefA_p1_sub2 = [242.3199/10240*100, 341.7056/10240*100, 323.5294/10240*100, 440.625/10240*100, 611.3191/10240*100, 813.3562/10240*100]
model_RefA_p2_sub2 = [2158.0189/10240*100, 2045.4545/10240*100, 2481.203/10240*100, 2120.6551/10240*100, 2143.9394/10240*100, 2367.1096/10240*100]
x = np.arange(len(x1_sub2)) 
line_model_our_p1_sub2 = ax2.plot(x, model_our_p1_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub2 = ax2.plot(x, model_our_p2_sub2, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub2 = ax2.plot(x, model_RefA_p1_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefA_p2_sub2 = ax2.plot(x, model_RefA_p2_sub2, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 70])
ax2.text(0.00, 62,'OSNs: 9')
ax2.text(0.00, 56,'Ethernet network: 10Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['244', '312', '352', '423', '566', '760']
model_our_p1_sub3 = [237.2925/10240*100, 258.3922/10240*100, 343.75/10240*100, 418.3149/10240*100, 545.9105/10240*100, 715.3614/10240*100]
model_our_p2_sub3 = [3450.9698/10240*100, 3922.4138/10240*100, 3690.0958/10240*100, 4550.7172/10240*100, 4220.8807/10240*100, 2032.3961/10240*100]
model_RefA_p1_sub3 = [237.2925/10240*100, 258.3922/10240*100, 343.75/10240*100, 418.3149/10240*100, 545.9105/10240*100, 715.3614/10240*100]
model_RefA_p2_sub3 = [3511.5132/10240*100, 4014.7059/10240*100, 3774.5098/10240*100, 4704.9788/10240*100, 4349.3852/10240*100, 2066.0729/10240*100]
x = np.arange(len(x1_sub3)) 
line_model_our_p1_sub3 = ax3.plot(x, model_our_p1_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub3 = ax3.plot(x, model_our_p2_sub3, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub3 = ax3.plot(x, model_RefA_p1_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub3 = ax3.plot(x, model_RefA_p2_sub3, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 70])
ax3.text(0.00, 62,'OSNs: 15')
ax3.text(0.00, 56,'Ethernet network: 10Gbps')
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

