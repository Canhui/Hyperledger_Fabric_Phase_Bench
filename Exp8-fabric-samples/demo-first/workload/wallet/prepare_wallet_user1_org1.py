import os

# Config info
user = "User1@org1.example.com"
mspid = "Org1MSP"
wallet_dir = os.environ['HOME']+"/fabric-samples/demo-first/workload/wallet/"
cert_file = open(os.environ['HOME']+"/fabric-samples/demo-first/crypto-config/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/signcerts/User1@org1.example.com-cert.pem","r")
key_file = open(os.environ['HOME']+"/fabric-samples/demo-first/crypto-config/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/priv_sk","r")

# Read files
lines1 = cert_file.readlines()
lines2 = key_file.readlines()

# --------------------------------------------------------
# Handle header one
result = ""
header1 = "{\"credentials\":{\"certificate\":\""
result = result + header1

# Handle body one
for line in lines1:
    result = result + line.strip('\n')+"\\n"

# --------------------------------------------------------
# Handle header two
result = result + "\",\"privateKey\":\""

# Handle body two
for line in lines2:
    result = result + line.strip('\n')+"\\r"+"\\n"

# --------------------------------------------------------
# Handle MSPID
result = result + "\"},\"mspId\":\""+mspid+"\",\"type\":\"X.509\",\"version\":1}"

# Print result of the user wallet
# print result

# Write into a file
output_file = open(wallet_dir+user+".id", "w")
output_file.write("%s" % result)

# Close Handler
output_file.close() # write close
cert_file.close() # read close
key_file.close() # read close
