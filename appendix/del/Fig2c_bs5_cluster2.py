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
model_our_p1_sub1 = [241.2975/10240*100, 320.7237/10240*100, 349.5763/10240*100, 483.6128/10240*100, 640.8514/10240*100, 881.8069/10240*100]
model_our_p2_sub1 = [1099.7596/10240*100, 1125/10240*100, 953.7572/10240*100, 909.547/10240*100, 1251.4741/10240*100, 1454.0816/10240*100]
model_RefA_p1_sub1 = [241.2975/10240*100, 320.7237/10240*100, 349.5763/10240*100, 483.6128/10240*100, 640.8514/10240*100, 881.8069/10240*100]
model_RefA_p2_sub1 = [1110.4369/10240*100, 1133.7209/10240*100, 964.9123/10240*100, 917.9688/10240*100, 1275.5409/10240*100, 1484.375/10240*100]
x = np.arange(len(x1_sub1)) 
line_model_our_p1_sub1 = ax1.plot(x, model_our_p1_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub1 = ax1.plot(x, model_our_p2_sub1, color='#000000', linestyle='dashed', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub1 = ax1.plot(x, model_RefA_p1_sub1, color='#CD853F', linestyle='solid', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub1 = ax1.plot(x, model_RefA_p2_sub1, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 108])
ax1.text(-0.10, 98,'OSNs: 3')
ax1.text(-0.10, 88,'Ethernet network: 10Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['244', '312', '352', '423', '566', '760']
model_our_p1_sub2 = [224.2647/10240*100, 279.1031/10240*100, 301.0949/10240*100, 414.8143/10240*100, 600.2545/10240*100, 873.1618/10240*100]
model_our_p2_sub2 = [4084.8214/10240*100, 3441.1765/10240*100, 3367.3469/10240*100, 3907.0197/10240*100, 3736.7958/10240*100, 4863.4812/10240*100]
model_RefA_p1_sub2 = [224.2647/10240*100, 279.1031/10240*100, 301.0949/10240*100, 414.8143/10240*100, 600.2545/10240*100, 873.1618/10240*100]
model_RefA_p2_sub2 = [4121.6216/10240*100, 3461.5385/10240*100, 3402.0619/10240*100, 3945.8955/10240*100, 3790.1786/10240*100, 4947.9167/10240*100]
x = np.arange(len(x1_sub2)) 
line_model_our_p1_sub2 = ax2.plot(x, model_our_p1_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub2 = ax2.plot(x, model_our_p2_sub2, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub2 = ax2.plot(x, model_RefA_p1_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefA_p2_sub2 = ax2.plot(x, model_RefA_p2_sub2, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 108])
ax2.text(-0.10, 98,'OSNs: 9')
ax2.text(-0.10, 88,'Ethernet network: 10Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['244', '312', '352', '423', '566', '760']
model_our_p1_sub3 = [228.75/10240*100, 285.6445/10240*100, 294.6429/10240*100, 434.8273/10240*100, 571.7942/10240*100, 860.5072/10240*100]
model_our_p2_sub3 = [7698.3173/10240*100, 7583.3333/10240*100, 6916.1677/10240*100, 7462.1976/10240*100, 8291.0156/10240*100, 10204.7521/10240*100]
model_RefA_p1_sub3 = [228.75/10240*100, 285.6445/10240*100, 294.6429/10240*100, 434.8273/10240*100, 571.7942/10240*100, 860.5072/10240*100]
model_RefA_p2_sub3 = [7773.0583/10240*100, 7639.9254/10240*100, 7000/10240*100, 7626.2019/10240*100, 8441.7614/10240*100, 10522.1519/10240*100]
x = np.arange(len(x1_sub3)) 
line_model_our_p1_sub3 = ax3.plot(x, model_our_p1_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_our_p2_sub3 = ax3.plot(x, model_our_p2_sub3, color='#000000', linestyle='solid', marker='s', markersize=8, linewidth=2.0)
line_model_RefA_p1_sub3 = ax3.plot(x, model_RefA_p1_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8,  linewidth=2.0)
line_model_RefA_p2_sub3 = ax3.plot(x, model_RefA_p2_sub3, color='#CD853F', linestyle='dashed', marker='x', markersize=8,  linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 108])
ax3.text(-0.10, 98,'OSNs: 15')
ax3.text(-0.10, 88,'Ethernet network: 10Gbps')
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

