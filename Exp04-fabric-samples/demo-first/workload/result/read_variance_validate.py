import os
import numpy as np

infile = os.environ['HOME']+"/fabric-samples/demo-first/workload/result/benchlog"


signal_submit_to_validate=["Get_Ordered_Transaction"]
signal_finished_from_validate=["Get_Committed_Transaction"]

timestamp_submit_to_validate=[]
timestamp_finished_from_validate=[]

interval_submit_to_validate=[]
interval_finished_from_validate=[]


with open(infile) as f:
    f = f.readlines()


for line in f:
    for phrase in signal_submit_to_validate: # Get timestamp submit to validate
        if phrase in line:
            if float(line.split(":")[1]) > 0:
                timestamp_submit_to_validate.append(float(line.split(":")[1]))
    for phrase in signal_finished_from_validate: # Get timestamp finished from validate
        if phrase in line:
            if float(line.split(":")[1]) > 0:
                timestamp_finished_from_validate.append(float(line.split(":")[1]))

for i in range(0, len(timestamp_submit_to_validate)-1): # Get interval submit to validate
    interval_submit_to_validate.append(timestamp_submit_to_validate[i+1]-timestamp_submit_to_validate[i])
for i in range(0, len(timestamp_finished_from_validate)-1): # Get interval finished from validate
    interval_finished_from_validate.append(timestamp_finished_from_validate[i+1]-timestamp_finished_from_validate[i])

for i in range(0, len(interval_submit_to_validate)): # Print interval submit to validate
    print interval_submit_to_validate[i]
for i in range(0, len(interval_finished_from_validate)): # Print interval finished from validate
    print interval_finished_from_validate[i]

print "variance of interval submit to validate: ", np.var(interval_submit_to_validate) # Calculate variance of interval submit to validate
print "variance of interval finished from validate: ", np.var(interval_finished_from_validate) # Calculate variance of interval finished from validate






    
#print arrival_submit[i+1]-arrival_submit[i]
#print arrival_submit[2]-arrival_submit[1]
#for i in range(1, len(arrival_submit)):
#    interval_submit[i-1] = arrival_submit[i] - arrival_submit[i-1];

#for i in range(0, len(interval_submit)):
#    print interval_submit[i]

#print "Mean_Delay_Endorse:"
#print float(sum(delays_endorse))/float(len(delays_endorse))

#print "Mean_Delay_Orderer:"
#print float(sum(delays_order))/float(len(delays_order))

#print "Mean_Delay_Commit:"
#print float(sum(delays_commit))/float(len(delays_commit))


# Sort the orderer delay
#delays_order_sorted = np.sort(delays_order)

# Calculate the proportional values of samples
#p = 1. * np.arange(len(delays_order)) / (len(delays_order) - 1)


# CDF, p = 0.5
#count = 0
#for i in p:
#    count = count + 1
#    if i >= 0.5:
#        print "CDF with the probability of 50%", delays_order_sorted[count]
#	break

# CDF, p = 0.9
#count = 0
#for i in p:
#    count = count + 1
#    if i >= 0.9:
#        print "CDF with the probability of 90%", delays_order_sorted[count]
#        break

# CDF, p = 0.95
#count = 0
#for i in p:
#    count = count + 1
#    if i >= 0.95:
#        print "CDF with the probability of 95%", delays_order_sorted[count]
#        break


#for i in delays_order:
#    print i

#print "Mean_Delay_order:"
#print float(sum(delays_order))/float(len(delays_order))
	     
#for i in delays_endorse:
#    print i

#for i in delays_order:
#    print i

#print "Lower_Bound_Phase_1:"
#print min(delays)

#print "Upper_Bound_Phase_1:"
#print max(delays)

#print "Mean_Delay_endorse:"
#print float(sum(delays_endorse))/float(len(delays_endorse))

#print "Mean_Delay_order:"
#print float(sum(delays_order))/float(len(delays_order))

#print "Std_Delay_Phrase_1:"
#print np.std(delays, ddof = 1)
