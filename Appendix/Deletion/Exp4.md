## Exp1: The Number of CPU Cores



一个peer，5个clients，一个orderer

项目的代码在：

Peer 有8 cpu cores



**Exp1.1:**

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
481 tps
0.155 s
vcpu 1: 15%
vcpu 2: 15%
vcpu 3: 15%
vcpu 4: 15%
vcpu 5: 15%
vcpu 6: 15%
vcpu 7: 15%
vcpu 8: 15%
```





**Exp1.2:**

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &

# client 2
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
886 tps
0.214 s
vcpu 1: 25%
vcpu 2: 25%
vcpu 3: 25%
vcpu 4: 25%
vcpu 5: 25%
vcpu 6: 25%
vcpu 7: 25%
vcpu 8: 25%
```





**Exp1.3:**

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &

# client 2
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &

# client 3
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
1274 tps
0.213 s
vcpu 1: 30%
vcpu 2: 30%
vcpu 3: 30%
vcpu 4: 30%
vcpu 5: 30%
vcpu 6: 30%
vcpu 7: 30%
vcpu 8: 30%
```





**Exp1.4:**

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &

# client 2
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &

# client 3
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &

# client 4
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
1474 tps
0.32 s
vcpu 1: 34%  
vcpu 2: 34%
vcpu 3: 34% 
vcpu 4: 34% 
vcpu 5: 34%
vcpu 6: 34%
vcpu 7: 34%
vcpu 8: 34%
```







**Exp1.5:**

ssh.sh的内容如下,

```shell
# client 1
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org2.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &

# client 2
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org3.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &

# client 3
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &
ssh peer0.org4.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; node invoke.js 30 400 100 1" &

# client 4
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org5.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &

# client 5
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
ssh peer0.org6.example.com "cd $HOME/fabric-samples/demo-first/workload/sdk-peer0-org1; nodejs invoke.js 30 400 100 1" &
```



运行命令如下，

```shell
$ ./ssh.sh > result/benchlog
```



查看execute phase的throughput, latency如下，

```shell
$ ./execute.sh
2257 tps
0.11 s
vcpu 1: 30%
vcpu 2: 30%
vcpu 3: 30%
vcpu 4: 30%
vcpu 5: 30%
vcpu 6: 30%
vcpu 7: 30%
vcpu 8: 30%
```









**Reference**

https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9354232













































