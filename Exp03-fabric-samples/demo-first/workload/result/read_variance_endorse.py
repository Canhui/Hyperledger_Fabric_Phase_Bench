import os
import numpy as np

infile = os.environ['HOME']+"/fabric-samples/demo-first/workload/result/benchlog"

signal_finished_from_endorse=["Get_Endorsed_Proposal"]
timestamp_finished_from_endorse=[]
interval_finished_from_endorse=[]

with open(infile) as f:
    f = f.readlines()

for line in f:
    for phrase in signal_finished_from_endorse: # Get timestamp finished from order
        if phrase in line:
            if float(line.split(":")[1]) > 0:
                timestamp_finished_from_endorse.append(float(line.split(":")[1]))

for i in range(0, len(timestamp_finished_from_endorse)-1): # Get interval finished from order
    interval_finished_from_endorse.append(timestamp_finished_from_endorse[i+1]-timestamp_finished_from_endorse[i])

for i in range(0, len(interval_finished_from_endorse)): # Print interval finished from order
    print interval_finished_from_endorse[i]

print "variance of interval finished from endorse: ", np.var(interval_finished_from_endorse) # Calculate variance of interval finished from endorser
