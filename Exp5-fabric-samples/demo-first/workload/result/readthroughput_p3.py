import os
infile = os.environ['HOME']+"/fabric-samples/demo-first/workload/result/peerlog"

signal_recv_time = ["Received block"]
signal_vlid_time = ["Validated block"]
signal_comt_time = ["Committed block"]

recv_time = []
vlid_time = []
comt_time = []
recv_blkid = []
txs_block = []

with open(infile) as f:
    f = f.readlines()

with open(infile) as f:
    f = f.readlines()

for line in f:
    for phrase in signal_recv_time:
        if phrase in line:
            recv_time.append(line.split(" ")[1])
            recv_blkid.append(line.split(" ")[11].replace('[','').replace(']',''))
    for phrase in signal_vlid_time:
        if phrase in line:
            vlid_time.append(line.split(" ")[1])
    for phrase in signal_comt_time:
        if phrase in line:
            comt_time.append(line.split(" ")[1])
            txs_block.append(line.split(" ")[13])

print "block id:"
for i in recv_blkid[-50:]:
    print i

print ""
print "number of txs in this block"
for i in txs_block[-50:]:
    print i

print ""
print "time a block received"
for i in recv_time[-50:]:
    print i

print ""
print "time a block validated"
for i in vlid_time[-50:]:
    print i

print ""
print "time a block committed"
for i in comt_time[-50:]:
    print i


#for line in f:
#    for phrase in signal_sendrate:
#        if phrase in line:
#	    send_time.append(float(line.split(":")[1]))
	     
#for i in send_time:
#    print i

#print "Avg_Send_Rate_Phrase_1:"
#print len(send_time)/(max(send_time)-min(send_time))
