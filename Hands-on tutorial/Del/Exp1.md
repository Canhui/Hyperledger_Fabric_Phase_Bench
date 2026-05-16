## Exp1: The Number of CPU Cores

一个peer，5个clients，一个orderer

项目的代码在：

Peer有1 cpu core

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
443 tps
0.180 s
vcpu 1: 45%
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
862 tps
0.206 s
vcpu 1: 60%
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
1301 tps
0.171 s
vcpu 1: 73%
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
1826 tps
0.11 s
vcpu 1: 83%
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
2200 tps
0.12 s
vcpu 1: 91%
```
