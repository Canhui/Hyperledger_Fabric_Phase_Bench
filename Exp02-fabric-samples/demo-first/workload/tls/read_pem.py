import os

def read(str):
    # Config info
    pem_dir = os.environ['HOME']+"/fabric-samples/demo-first/crypto-config/peerOrganizations/"+str+".example.com/tlsca/tlsca."+str+".example.com-cert.pem"
    pem = open(pem_dir,"r")

    # Read files
    lines = pem.readlines()

    # Handle body
    result = ""
    for line in lines:
        result = result + line.strip('\n')+"\\n"
    #print result

    # Read close
    pem.close()    
    return result
