import os
infile = os.environ['HOME']+"/fabric-samples/demo-first/workload/result/ordererlog"

new_block=["Broadcasting about update blockfilesInfo"]
block_id=[]
create_time=[]

with open(infile) as f:
    f = f.readlines()

for line in f:
    for phrase in new_block:
        if phrase in line:
            # print line.split(" ")[1] # creation timestamp
            # print line.split(" ")[15] # block id
            block_id.append(line.split(" ")[15]) # block id
            create_time.append(line.split(" ")[1])

print "Block_ID:"
for i in block_id[-50:]:
    print i

print "Block_Time:"
for i in create_time[-50:]:
    print i
