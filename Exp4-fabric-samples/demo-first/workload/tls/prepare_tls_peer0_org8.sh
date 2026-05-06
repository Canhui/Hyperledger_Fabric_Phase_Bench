# org info
org_name="Org8"
org_msp="Org8MSP"
tls_file=`python -c 'import read_pem; print read_pem.read("org8")'`

# peer info
peer_name="peer0.org8.example.com"
peer_addr="grpcs://peer0.org8.example.com:7051"
file_name="connection-peer0-org8.json"

# details
cat>$HOME/fabric-samples/demo-first/workload/tls/$file_name<<EOF
{
    "name": "test-network-org1",
    "version": "1.0.0",
    "client": {
        "organization": "$org_name",
        "connection": {
            "timeout": {
                "peer": {
                    "endorser": "300"
                }
            }
        }
    },
    "organizations": {
        "$org_name": {
            "mspid": "$org_msp",
            "peers": [
                "$peer_name"
            ]
        }
    },
    "peers": {
        "$peer_name": {
            "url": "$peer_addr",
            "tlsCACerts": {
                "pem": "$tls_file"
            },
            "grpcOptions": {
                "ssl-target-name-override": "$peer_name",
                "hostnameOverride": "$peer_name"
            }
        }
    }
}
EOF

rm -rf *.pyc
