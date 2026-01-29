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
model_our_sub1 = [34.5325/1024*100, 32.6849/1024*100, 27.0958/1024*100, 26.0451/1024*100, 27.2372/1024*100, 26.4516/1024*100, 27.7423/1024*100, 32.9142/1024*100]
model_RefA_sub1 = [34.5691/1024*100, 32.7088/1024*100, 27.1191/1024*100, 26.0723/1024*100, 27.2765/1024*100, 26.5077/1024*100, 27.9362/1024*100, 34.4636/1024*100]
model_RefB_sub1 = [34.5569/1024*100, 32.7008/1024*100, 27.1051/1024*100, 26.0621/1024*100, 27.2584/1024*100, 26.4784/1024*100, 27.8401/1024*100, 33.6695/1024*100]
x = np.arange(len(x1_sub1)) 
line_model_our_sub1 = ax1.plot(x, model_our_sub1, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub1 = ax1.plot(x, model_RefA_sub1, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub1 = ax1.plot(x, model_RefB_sub1, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax1.set_xticks(x)
ax1.set_xticklabels(x1_sub1)
ax1.set_ylim([0, 30])
ax1.text(0.00, 27,'CPU cores: 1')
ax1.text(0.00, 24,'Ethernet network: 1Gbps')
ax1.tick_params(axis='both', which='major', labelsize=7)

# data sub2
x1_sub2 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
model_our_sub2 = [83.6212/1024*100, 86.5754/1024*100, 84.0082/1024*100, 69.9675/1024*100, 79.4618/1024*100, 80.2338/1024*100, 78.9255/1024*100,73.3912/1024*100]
model_RefA_sub2 = [83.4814/1024*100, 86.6537/1024*100, 84.0789/1024*100, 70.0534/1024*100, 81.8056/1024*100, 80.4499/1024*100, 79.3134/1024*100, 73.8606/1024*100]
model_RefB_sub2 = [83.4814/1024*100, 86.6276/1024*100, 84.0436/1024*100, 70.0152/1024*100, 81.7275/1024*100, 80.3468/1024*100, 79.1282/1024*100, 73.633/1024*100]
x = np.arange(len(x1_sub2)) 
line_model_our_sub2 = ax2.plot(x, model_our_sub2, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub2 = ax2.plot(x, model_RefA_sub2, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub2 = ax2.plot(x, model_RefB_sub2, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax2.set_xticks(x)
ax2.set_xticklabels(x1_sub2)
ax2.set_ylim([0, 30])
ax2.text(0.00, 27,'CPU cores: 2')
ax2.text(0.00, 24,'Ethernet network: 1Gbps')
ax2.tick_params(axis='both', which='major', labelsize=7)

# data sub3
x1_sub3 = ['426', '613', '852', '1095', '1278', '1338', '1446', '1478']
model_our_sub3 = [112.5634/1024*100, 132.9065/1024*100, 125.827/1024*100, 151.2765/1024*100, 155.4392/1024*100, 143.4227/1024*100, 163.8812/1024*100, 130.4977/1024*100]
model_RefA_sub3 = [112.5634/1024*100, 132.9065/1024*100, 125.827/1024*100, 151.3211/1024*100, 155.5199/1024*100, 143.4883/1024*100, 163.9604/1024*100, 130.5469/1024*100]
model_RefB_sub3 = [112.5634/1024*100, 132.9065/1024*100, 125.827/1024*100, 151.3211/1024*100, 155.4795/1024*100, 143.4555/1024*100, 163.9604/1024*100, 130.5469/1024*100]
x = np.arange(len(x1_sub3)) 
line_model_our_sub3 = ax3.plot(x, model_our_sub3, color='#000000', linestyle='solid', marker='o', markersize=8, linewidth=2.0)
line_model_RefA_sub3 = ax3.plot(x, model_RefA_sub3, color='#CD853F', linestyle='dashed', marker='*', markersize=8, linewidth=2.0)
line_model_RefB_sub3 = ax3.plot(x, model_RefB_sub3, color='#00BFFF', linestyle='dashed', marker='.', markersize=8, linewidth=2.0)
ax3.set_xticks(x)
ax3.set_xticklabels(x1_sub3)
ax3.set_ylim([0, 30])
ax3.text(0.00, 27,'CPU cores: 4')
ax3.text(0.00, 24,'Ethernet network: 1Gbps')
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

