## Exp1: The Number of CPU Cores

一个peer，5个clients，一个orderer

项目的代码在：

Peer 有2 cpu cores

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
465 tps
0.156 s
vcpu 1: 33%
vcpu 2: 34%
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
885 tps
0.10 s
vcpu 1: 39%
vcpu 2: 39%
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
1400 tps
0.11 s
vcpu 1: 45%
vcpu 2: 45%
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
1677 tps
0.237 s
vcpu 1: 60%
vcpu 2: 60% 
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
2046 tps
0.22 s
vcpu 1: 56%
vcpu 2: 56%
```

**Reference**

https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9354232
