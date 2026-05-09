# node invoke.js tasks_per_batch delay_per_batch rounds bytes_per_transaction

#ssh peer0.org1.example.com "echo 'hi'"
#ssh peer0.org2.example.com "echo 'hi'"

ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 10 500 10 1" &



#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 10 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 10 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 10 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 100 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 100 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 100 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 100 1" &
#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 60 100 100 1" &

#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 300 10 50 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org2; nodejs invoke.js 30 400 100 1" &
#ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org3; node invoke.js 30 400 100 1" &
#ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org4; node invoke.js 30 400 100 1" &
#ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org5; nodejs invoke.js 30 400 100 1" &


#ssh peer0.org1.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 320 1 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org2; nodejs invoke.js 30 320 1 1" &
#ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org3; node invoke.js 30 320 1 1" &
#ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org4; node invoke.js 30 320 1 1" &
#ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org5; nodejs invoke.js 30 320 1 1" &

