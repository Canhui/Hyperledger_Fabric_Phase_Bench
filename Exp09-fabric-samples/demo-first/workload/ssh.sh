# node invoke.js tasks_per_batch delay_per_batch rounds bytes_per_transaction

#ssh peer0.org1.example.com "echo 'hi'"
#ssh peer0.org2.example.com "echo 'hi'"

#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 1" &

#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 10" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 10" &

ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 100" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 100" &

