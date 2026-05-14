## 1. Hands-on Tutorial
Please find the Hands-on Tutorial in [MS Doc](https://www.reference.com) or in [PDF](https://www.reference.com).




## 2. Preparation

#### 2.1. Cluster Environment

Please see section A of the tutorial for preparation of multiple computing nodes on the cloud.


#### 2.2. Single-Node Test

Please see section B of the tutorial for preparation of single-node test of Hyperledger Fabric network.


#### 2.3. Workload Generator

<ul>
  <li> Q1: How to generate a transaction via Node.js SDK?
    <ul>
      <li>For invoke a transaction, please see invoke.js under the workload folder.</li>
      <li>For query a transaction, please see query.js under the worklaod folder.</li>
    </ul>
  </li>

  <li> Q2: How to generate some transactions using a client?
    <ul>
      <li>For invoke some transactions, please see ssh.sh under the workload folder.</li>
      <li>For query some transactions, please see ssh.sh under the worklaod folder.</li>
    </ul>
  </li>

  <li> Q3: How to stably generate many transactions using many clients?
    <ul>
      <li>For stably invoke many transactions, please see ssh.sh under the workload folder.</li>
      <li>For stably query many transactions, please see ssh.sh under the worklaod folder.</li>
    </ul>
  </li>
</ul>



## 3. Experiments

#### 3.1. Multiple-Nodes Test

Please see section 1, 2, 3 of the tutorial for multiple-nodes test of Hyperledger Fabric.

#### 3.2. Multiple-Nodes Run

Please see section 4 of the tutorial for multiple-nodes running of Hyperledger Fabric, e.g., 7 CLI on 7 endorsing peers, 1 non-endorsing peer, 15 ordering service nodes.

#### 3.3. Dynamic Adjustment of Block Parameters

Please see section 5 of the tutorial for dynamic adjustment of block parameters on single ordering service node; section 6 for dynamic adjustment of block parameters on multiple ordering service nodes; section 7 for dynamic adjustment of block parameters on single peer; and section 8 for dynamic adjustment of block parameters on multiple peers.

#### 3.4. Different Transaction Payoff Sizes 

Please see section 9 of the tutorial for different transaction payoff sizes.

#### 3.5. Different Chaincodes 

Please see section 10 of the tutorial for different chaincodes.



## 4. Numerical Results

#### 4.1. Execute Phase in Cluster 1

<p align="center">Table 1. Throughput and latency of an endorsing peer with $c=1, 2, 4$ CPU cores in cluster 1</p>

|      | Measure derived |         |          |         |             |                  |                   | Measure             |          |          |                      |            |          |                        |              |          |                     | Our Model |               |                 |
| ---- | --------------- | ------- | -------- | ------- | ----------- | ---------------- | ----------------- | ------------------- | -------- | -------- | -------------------- | ---------- | -------- | ---------------------- | ------------ | -------- | ------------------- | --------- | ------------- | --------------- |
| $c$  | $\lambda^e$     | $\mu^e$ | $\rho^e$ | $T_s^e$ | Our $T_q^e$ | $M/M/1$  $T_q^e$ | $M/H_2/1$ $T_q^e$ | Our $T_{comm}^e$    | Our BW   | avg BW   | $M/M/1$ $T_{comm}^e$ | $M/M/1$ BW | avg BW   | $M/H_2/1$ $T_{comm}^e$ | $M/H_2/1$ BW | avg BW   | $T^e$               | Our $T^e$ | $M/M/1$ $T^e$ | $M/H_2/1$ $T^e$ |
| 1    | 209             | 780     | 0.2679   | 0.0013  | 0.0002      | 0.0005           | 0.0004            | 0.2837 $\pm$ 0.0103 | 34.5325  | 29.3380  | 0.2834 $\pm$ 0.0103  | 34.5691    | 29.5817  | 0.2835 $\pm$ 0.0103    | 34.5569      | 29.4589  | 0.2852 $\pm$ 0.0103 | 0.3354    | 0.3330        | 0.3343          |
| 1    | 287             | 780     | 0.3679   | 0.0013  | 0.0004      | 0.0007           | 0.0006            | 0.4116 $\pm$ 0.0145 | 32.6849  | 29.3380  | 0.4113 $\pm$ 0.0145  | 32.7088    | 29.5817  | 0.4114 $\pm$ 0.0145    | 32.7008      | 29.4589  | 0.4133 $\pm$ 0.0145 | 0.4603    | 0.4568        | 0.4586          |
| 1    | 337             | 780     | 0.4321   | 0.0013  | 0.0005      | 0.0010           | 0.0007            | 0.5830 $\pm$ 0.0291 | 27.0958  | 29.3380  | 0.5825 $\pm$ 0.0291  | 27.1191    | 29.5817  | 0.5828 $\pm$ 0.0291    | 27.1051      | 29.4589  | 0.5848 $\pm$ 0.0291 | 0.5402    | 0.5363        | 0.5382          |
| 1    | 426             | 780     | 0.5462   | 0.0013  | 0.0007      | 0.0015           | 0.0012            | 0.7667 $\pm$ 0.0741 | 26.0451  | 29.3380  | 0.7659 $\pm$ 0.0741  | 26.0723    | 29.5817  | 0.7662 $\pm$ 0.0741    | 26.0621      | 29.4589  | 0.7687 $\pm$ 0.0741 | 0.6826    | 0.6778        | 0.6804          |
| 1    | 524             | 780     | 0.6718   | 0.0013  | 0.0013      | 0.0026           | 0.0020            | 0.9018 $\pm$ 0.0904 | 27.2372  | 29.3380  | 0.9005 $\pm$ 0.0904  | 27.2765    | 29.5817  | 0.9011 $\pm$ 0.0904    | 27.2584      | 29.4589  | 0.9044 $\pm$ 0.0904 | 0.8398    | 0.8342        | 0.8371          |
| 1    | 613             | 780     | 0.7859   | 0.0013  | 0.0024      | 0.0047           | 0.0035            | 1.0863 $\pm$ 0.1982 | 26.4516  | 29.3380  | 1.0840 $\pm$ 0.1982  | 26.5077    | 29.5817  | 1.0852 $\pm$ 0.1982    | 26.4784      | 29.4589  | 1.0900 $\pm$ 0.1982 | 0.9831    | 0.9774        | 0.9802          |
| 1    | 725             | 780     | 0.9295   | 0.0013  | 0.0084      | 0.0169           | 0.0127            | 1.2250 $\pm$ 0.2908 | 27.7423  | 29.3380  | 1.2165 $\pm$ 0.2908  | 27.9362    | 29.5817  | 1.2207 $\pm$ 0.2908    | 27.8401      | 29.4589  | 1.2347 $\pm$ 0.2908 | 1.1681    | 1.1670        | 1.1676          |
| 1    | 770             | 780     | 0.9872   | 0.0013  | 0.0494      | 0.0987           | 0.0740            | 1.0966 $\pm$ 0.2199 | 32.9142  | 29.3380  | 1.0473 $\pm$ 0.2199  | 34.4636    | 29.5817  | 1.0720 $\pm$ 0.2199    | 33.6695      | 29.4589  | 1.1473 $\pm$ 0.2199 | 1.2810    | 1.3201        | 1.3005          |
| 2    | 426             | 780     | 0.2731   | 0.0013  | 0.0006      | 0.0002           | 0.0002            | 0.2388 $\pm$ 0.0173 | 83.6212  | 79.5231  | 0.2392 $\pm$ 0.0173  | 83.4814    | 79.9621  | 0.2392 $\pm$ 0.0173    | 83.4814      | 79.8754  | 0.2407 $\pm$ 0.0173 | 0.2530    | 0.2512        | 0.2515          |
| 2    | 613             | 780     | 0.3929   | 0.0013  | 0.0001      | 0.0004           | 0.0003            | 0.3319 $\pm$ 0.0173 | 86.5754  | 79.5231  | 0.3316 $\pm$ 0.0173  | 86.6537    | 79.9621  | 0.3317 $\pm$ 0.0173    | 86.6276      | 79.8754  | 0.3333 $\pm$ 0.0573 | 0.3627    | 0.3610        | 0.3613          |
| 2    | 852             | 780     | 0.5462   | 0.0013  | 0.0003      | 0.0007           | 0.0005            | 0.4754 $\pm$ 0.0173 | 84.0082  | 79.5231  | 0.4750 $\pm$ 0.0173  | 84.0789    | 79.9621  | 0.4752 $\pm$ 0.0173    | 84.0436      | 79.8754  | 0.4770 $\pm$ 0.0928 | 0.5038    | 0.5015        | 0.5018          |
| 2    | 1095            | 780     | 0.7019   | 0.0013  | 0.0006      | 0.0015           | 0.0011            | 0.7336 $\pm$ 0.0173 | 69.9675  | 79.5231  | 0.7327 $\pm$ 0.0173  | 70.0534    | 79.9621  | 0.7331 $\pm$ 0.0173    | 70.0152      | 79.8754  | 0.7355 $\pm$ 0.1612 | 0.6473    | 0.6447        | 0.6450          |
| 2    | 1278            | 780     | 0.8192   | 0.0013  | 0.0013      | 0.0029           | 0.0022            | 0.7539 $\pm$ 0.0173 | 79.4618  | 79.5231  | 0.7323 $\pm$ 0.0173  | 81.8056    | 79.9621  | 0.7330 $\pm$ 0.0173    | 81.7275      | 79.8754  | 0.7565 $\pm$ 0.2216 | 0.7559    | 0.7534        | 0.7535          |
| 2    | 1338            | 780     | 0.8577   | 0.0013  | 0.0018      | 0.0039           | 0.0029            | 0.7817 $\pm$ 0.0173 | 80.2338  | 79.5231  | 0.7796 $\pm$ 0.0173  | 80.4499    | 79.9621  | 0.7806 $\pm$ 0.0173    | 80.3468      | 79.8754  | 0.7848 $\pm$ 0.2273 | 0.7918    | 0.7896        | 0.7894          |
| 2    | 1446            | 780     | 0.9269   | 0.0013  | 0.0039      | 0.0081           | 0.0061            | 0.8588 $\pm$ 0.0173 | 78.9255  | 79.5231  | 0.8546 $\pm$ 0.0173  | 79.3134    | 79.9621  | 0.8566 $\pm$ 0.0173    | 79.1282      | 79.8754  | 0.8640 $\pm$ 0.2406 | 0.8575    | 0.8571        | 0.8560          |
| 2    | 1478            | 780     | 0.9474   | 0.0013  | 0.0056      | 0.0116           | 0.0087            | 0.9440 $\pm$ 0.0173 | 73.3912  | 79.5231  | 0.9380 $\pm$ 0.0173  | 73.8606    | 79.9621  | 0.9409 $\pm$ 0.0173    | 73.6330      | 79.8754  | 0.9509 $\pm$ 0.1122 | 0.8781    | 0.8793        | 0.8774          |
| 4    | 426             | 780     | 0.1365   | 0.0013  | 0.0000      | 0.0000           | 0.0000            | 0.1774 $\pm$ 0.0143 | 112.5634 | 139.4768 | 0.1774 $\pm$ 0.0143  | 112.5634   | 139.5167 | 0.1774 $\pm$ 0.0143    | 112.5634     | 139.5076 | 0.1787 $\pm$ 0.0143 | 0.1445    | 0.1444        | 0.1444          |
| 4    | 613             | 780     | 0.1965   | 0.0013  | 0.0000      | 0.0000           | 0.0000            | 0.2162 $\pm$ 0.0277 | 132.9065 | 139.4768 | 0.2162 $\pm$ 0.0277  | 132.9065   | 139.5167 | 0.2162 $\pm$ 0.0277    | 132.9065     | 139.5076 | 0.2175 $\pm$ 0.0277 | 0.2073    | 0.2073        | 0.2073          |
| 4    | 852             | 780     | 0.2731   | 0.0013  | 0.0000      | 0.0000           | 0.0000            | 0.3174 $\pm$ 0.0323 | 125.8270 | 139.4768 | 0.3174 $\pm$ 0.0323  | 125.8270   | 139.5167 | 0.3174 $\pm$ 0.0323    | 125.8270     | 139.5076 | 0.3187 $\pm$ 0.0323 | 0.2876    | 0.2876        | 0.2876          |
| 4    | 1095            | 780     | 0.3510   | 0.0013  | 0.0000      | 0.0001           | 0.0001            | 0.3393 $\pm$ 0.0632 | 151.2765 | 139.4768 | 0.3392 $\pm$ 0.0632  | 151.3211   | 139.5167 | 0.3392 $\pm$ 0.0632    | 151.3211     | 139.5076 | 0.3406 $\pm$ 0.0632 | 0.3693    | 0.3693        | 0.3693          |
| 4    | 1278            | 780     | 0.4096   | 0.0013  | 0.0000      | 0.0002           | 0.0001            | 0.3854 $\pm$ 0.0748 | 155.4392 | 139.4768 | 0.3852 $\pm$ 0.0748  | 155.5199   | 139.5167 | 0.3853 $\pm$ 0.0748    | 155.4795     | 139.5076 | 0.3867 $\pm$ 0.0748 | 0.4308    | 0.4309        | 0.4308          |
| 4    | 1338            | 780     | 0.4288   | 0.0013  | 0.0000      | 0.0002           | 0.0001            | 0.4373 $\pm$ 0.1653 | 143.4227 | 139.4768 | 0.4371 $\pm$ 0.1653  | 143.4883   | 139.5167 | 0.4372 $\pm$ 0.1653    | 143.4555     | 139.5076 | 0.4386 $\pm$ 0.1653 | 0.4510    | 0.4510        | 0.4510          |
| 4    | 1446            | 780     | 0.4635   | 0.0013  | 0.0000      | 0.0002           | 0.0002            | 0.4136 $\pm$ 0.1778 | 163.8812 | 139.4768 | 0.4134 $\pm$ 0.1778  | 163.9604   | 139.5167 | 0.4134 $\pm$ 0.1778    | 163.9604     | 139.5076 | 0.4149 $\pm$ 0.1778 | 0.4873    | 0.4873        | 0.4874          |
| 4    | 1478            | 780     | 0.4737   | 0.0013  | 0.0000      | 0.0002           | 0.0002            | 0.5309 $\pm$ 0.2986 | 130.4977 | 139.4768 | 0.5307 $\pm$ 0.2986  | 130.5469   | 139.5167 | 0.5307 $\pm$ 0.2986    | 130.5469     | 139.5076 | 0.5322 $\pm$ 0.2986 | 0.4980    | 0.4981        | 0.4981          |

Table 1 shows the throughput and latency of an endorsing peer with $c=1, 2, 4$ CPU core(s) in cluster 1. It validates the performance mode of throughput and latency in the execute phase. The details of performance metrics are as follows:

<ul>

  <li> Performance metric - $c$
    <ul>
      <li> Explanation: The number of CPU cores in the execute phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\lambda^e$
    <ul>
      <li> Explanation: The transaction arrival rate in transactions per second in the execute phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\mu^e$
    <ul>
      <li> Explanation: The maximum throughput of an endorsing peer with a single CPU core in the execute phase.</li>
      <li> Example 1: The maximum throughput of an endorsing peer with a single CPU core, i.e., $c=1$, is $\mu^e=780$ transactions per second.</li>
    </ul>
  </li>

  <li> Performance metric - $\rho^e$
    <ul>
      <li> Explanation: The utilization of an endorsing peer in the execute phase, where we can derive $\rho^e=\lambda^e/(c\mu^e)$.</li>
      <li> Example 1: The maximum throughput of an endorsing peer with a single CPU core, i.e., $c=1$, is $\mu^e=780$ transactions per second.</li>
    </ul>
  </li>

  <li> Performance metric - $T_s^e$
    <ul>
      <li> Explanation: The service time of a transaction in the execute phase, where we can derive $T_s^e=1/mu^e$.</li>
    </ul>
  </li>

  <li> Performance metric - $T_q^e$
    <ul>
      <li> Explanation: The queueing latency of a transaction in the execute phase.</li>
    </ul>
  </li>

  <li> Performance metric - $T_{comm}^e$
    <ul>
      <li> Explanation: The communication latency of a transaction in the execute phase, where we measure the overall latency $T^e$, and we can derive $T_{comm}^e=T^e-T_s^e-T_q^e$.</li>
    </ul>
  </li>

</ul>


The maximum throughput of an endorsing peer with a single CPU, i.e., $c=1$, is $\mu^e=780$ transactions per second, meaning that the service time of a transaction is $T_s^e=0.0013$ seconds. 

We use two examples to explain the details. 

Communication Latency Calculations (Example One):

In example one, let the number of CPU cores $c=1$ and the transaction arrival rate $\lambda^e=209$ transactions per second, we have the queueing latency $T_q^e=0.0002$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.2852$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.2852-0.0013-0.0002=0.2837$ seconds. 










 It validates the model of throughput and latency in the execute phase. The maximum throughput of an endorsing peer with a single CPU core is $\mu^e=780$ transactions per second, meaning that the service time of a transaction is $T_s^e=0.0013$ seconds. We use two examples to explain the table. In example one, let the number of CPU cores $c=1$ and the transaction arrival rate $\lambda^e=209$ transactions per second, we have the queueing latency $T_q^e=0.0002$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.2852$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.2852-0.0013-0.0002=0.2837$ seconds. 




















## License

Fabric_Phase_Bench source code is available under the MIT License 2026.


## Reference
[1. Hyperledger Fabric] https://github.com/hyperledger/fabric/tree/v2.2.0 <br>
[2. Hyperledger Fabric Dynamic Channel Update] https://hyperledger-fabric.readthedocs.io/en/release-2.2/config_update.html <br>
[3. Hyperledger Fabric SDK for node.js] https://hyperledger.github.io/fabric-sdk-node/release-1.4/module-fabric-network.html
