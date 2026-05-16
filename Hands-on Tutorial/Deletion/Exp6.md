## Exp5: The SSD Orderer



一个peer，1个client，一个orderer

项目的代码在

Ali Cloud的产品型号如下，

本地SSD型 i3g

ecs.i3g.2xlarge

Intel Xeon(Cascade Lake) Platinum 8269CY



**Exp1.1:**

Block size: 10

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
#ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
Avg_Send_Rate_Phrase_1:
480.927317146

Mean_Delay_Orderer:
0.0273634635889
```



查看硬盘IOPS, Write Rate如下，

```shell
$ iostat -x 3
w/s rkB/s
437.33     6669.33
```





查看execute phase的throughput如下，

```shell
// orderer
$ docker logs $(docker ps -a | grep 'orderer'| awk '{print $1 }') >& ordererlog
$ python readthroughput_p2.py

// peer
$ docker logs $(docker ps -a | grep 'peer node start'| awk '{print $1 }') >& peerlog
$ python readthroughput_p3.py

454 tps
```



















































