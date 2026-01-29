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
x1_sub1 = ['214', '244', '312', '352', '423', '460']
model_our_sub1 = [47.2059/10240*100, 46.76/10240*100, 46.0195/10240*100, 39.6158/10240*100, 37.8833/10240*100, 37.7297/10240*100]
model_RefA_sub1 = [47.4067/10240*100, 46.9906/10240*100, 46.3256/10240*100, 39.9129/10240*100, 38.5836/10240*100,41.2679/10240*100]
model_RefB_sub1 = [47.2949/10240*100, 46.875/10240*100, 46.1793/10240*100, 39.7686/10240*100, 38.2339/10240*100, 39.4196/10240*100]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 5])
ax1.text(0.00, 4.4,'CPU cores: 1')
ax1.text(0.00, 3.9,'Ethernet network: 10Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['244', '312', '352', '423', '460', '566', '670']
model_our_sub2 = [130.1195/10240*100, 139.0209/10240*100, 129.108/10240*100, 119.2311/10240*100, 126.1703/10240*100, 139.0527/10240*100, 153.7261/10240*100]
model_RefA_sub2 = [130.5651/10240*100, 139.5515/10240*100, 129.6151/10240*100, 119.6628/10240*100, 126.6892/10240*100, 139.7853/10240*100, 154.8632/10240*100]
model_RefB_sub2 = [130.4162/10240*100, 139.2857/10240*100, 129.4118/10240*100, 119.5185/10240*100, 126.4663/10240*100, 139.4913/10240*100, 154.4063/10240*100]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 5])
ax2.text(0.00, 4.4,'CPU cores: 2')
ax2.text(0.00, 3.9,'Ethernet network: 10Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['244', '312', '352', '423', '460', '566', '670']
model_our_sub3 = [166.9708/10240*100, 194.2231/10240*100, 215.1239/10240*100, 249.097/10240*100, 233.8666/10240*100, 249.1197/10240*100, 275.0109/10240*100]
model_RefA_sub3 = [166.9708/10240*100, 194.4814/10240*100, 215.4047/10240*100, 249.4104/10240*100, 234.1205/10240*100, 249.5884/10240*100,275.4934/10240*100]
model_RefB_sub3 = [166.9708/10240*100, 194.2231/10240*100, 215.1239/10240*100, 249.4104/10240*100, 234.1205/10240*100, 249.3539/10240*100, 275.4934/10240*100]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub3 = ax3.plot(x, model_RefB_sub3, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 5])
ax3.text(0.00, 4.4,'CPU cores: 4')
ax3.text(0.00, 3.9,'Ethernet network: 10Gbps')
ax3.tick_params(axis='both', which='major', labelsize=7)

# function to show the plot
fig.text(0.5, 0.020, 'Transaction arrival rate $\lambda^e$ (tps)', ha='center', va='center', fontsize = 9)
fig.text(0.020, 0.5, 'Bandwidth utility (%)', ha='center', va='center', rotation='vertical', fontsize = 9)
fig.legend([line_model_our_sub1, line_model_RefA_sub1, line_model_RefB_sub1],     # The line objects
           labels = [r'Our model $\beta^e$', r'$M/M/1$ model $\beta^e$', r'$M/H_2/1$ model $\beta^e$'],
           ncol = 3,
           loc="upper center",   # Position of legend
           frameon=False,
           fontsize = 9
           )
plt.show() 

