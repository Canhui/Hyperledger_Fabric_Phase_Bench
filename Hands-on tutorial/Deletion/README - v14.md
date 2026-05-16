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




## 4. Numerical Calculations and Results

#### 4.1. Execute Phase in Cluster 1

Table 1. Throughput and latency of an endorsing peer with $c=1, 2, 4$ CPU cores in cluster 1

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
      <li> Example 1: The maximum throughput of an endorsing peer with a single CPU core, i.e., $c=1$, is $\mu^e=780$ transactions per second,  $\lambda^e=209$ transactions per second, and hence $\rho^e=\lambda^e/(c\mu^e)=209/(1*780)=0.2679$.</li>
    </ul>
  </li>

  <li> Performance metric - $T_s^e$
    <ul>
      <li> Explanation: The service time of a transaction in the execute phase, where we can derive $T_s^e=1/ \mu^e$.</li>
      <li> Example 1: The service time of a transaction in the execute phase, where we can derive $T_s^e=1/ \mu^e=1/780=0.0013$ seconds.</li>
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
      <li> Example 1: The number of CPU cores $c=1$ and the transaction arrival rate $\lambda^e=209$ transactions per second, we have the queueing latency $T_q^e=0.0002$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.2852$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.2852-0.0013-0.0002=0.2837$ seconds. And when $c=1$, the average effective network bandwidth is stable around $\beta^e=29.3380$ Mbps, from which the model has an overall latency $T^e=0.3354$ seconds.</li>
      <li> Example 2: The number of CPU cores $c=2$ and the transaction arrival rate $\lambda^e=426$ transactions per second, we have the queueing latency $T_q^e=0.0006$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.2407$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.2388$ seconds. And when $c=2$, the average effective network bandwidth is stable around $\beta^e=79.5231$ Mbps, from which the model has an overall latency $T^e=0.2530$ seconds.</li>
    </ul>
  </li>

</ul>


#### 4.2. Execute Phase in Cluster 2

Table 2. The throughput and latency of an endorsing peer with $c=$1,2,4 CPU cores in cluster 2.

|      | Measure derived |         |          |         |             |                 |                   | Measure             |          |          |                      |            |          |                        |              |          |                     | Our model |               |                 |
| ---- | --------------- | ------- | -------- | ------- | ----------- | --------------- | ----------------- | ------------------- | -------- | -------- | -------------------- | ---------- | -------- | ---------------------- | ------------ | -------- | ------------------- | --------- | ------------- | --------------- |
| $c$  | $\lambda^e$     | $\mu^e$ | $\rho^e$ | $T_s^e$ | Our $T_q^e$ | $M/M/1$ $T_q^e$ | $M/H_2/1$ $T_q^e$ | Our $T_{comm}^e$    | Our BW   | avg BW   | $M/M/1$ $T_{comm}^e$ | $M/M/1$ BW | avg BW   | $M/H_2/1$ $T_{comm}^e$ | $M/H_2/1$ BW | avg BW   | $T^e$               | Our $T^e$ | $M/M/1$ $T^e$ | $M/H_2/1$ $T^e$ |
| 1    | 214             | 470     | 0.4553   | 0.0021  | 0.0009      | 0.0018          | 0.0013            | 0.2125 $\pm$ 0.0128 | 47.2059  | 42.5357  | 0.2116 $\pm$ 0.0128  | 47.4067    | 43.4146  | 0.2121 $\pm$ 0.0128    | 47.2949      | 42.9619  | 0.2155 $\pm$ 0.0128 | 0.2388    | 0.2350        | 0.2369          |
| 1    | 244             | 470     | 0.5191   | 0.0021  | 0.0011      | 0.0023          | 0.0017            | 0.2446 $\pm$ 0.0359 | 46.7600  | 42.5357  | 0.2434 $\pm$ 0.0359  | 46.9906    | 43.4146  | 0.2440 $\pm$ 0.0359    | 46.8750      | 42.9619  | 0.2478 $\pm$ 0.0359 | 0.2721    | 0.2678        | 0.2700          |
| 1    | 312             | 470     | 0.6638   | 0.0021  | 0.0021      | 0.0042          | 0.0032            | 0.3178 $\pm$ 0.0241 | 46.0195  | 42.5357  | 0.3157 $\pm$ 0.0241  | 46.3256    | 43.4146  | 0.3167 $\pm$ 0.0241    | 46.1793      | 42.9619  | 0.3220 $\pm$ 0.0241 | 0.3480    | 0.3432        | 0.3457          |
| 1    | 352             | 470     | 0.7489   | 0.0021  | 0.0032      | 0.0063          | 0.0048            | 0.4165 $\pm$ 0.0764 | 39.6158  | 42.5357  | 0.4134 $\pm$ 0.0764  | 39.9129    | 43.4146  | 0.4149 $\pm$ 0.0764    | 39.7686      | 42.9619  | 0.4218 $\pm$ 0.0764 | 0.3932    | 0.3885        | 0.3910          |
| 1    | 423             | 470     | 0.9000   | 0.0021  | 0.0096      | 0.0191          | 0.0144            | 0.5234 $\pm$ 0.0772 | 37.8833  | 42.5357  | 0.5139 $\pm$ 0.0772  | 38.5836    | 43.4146  | 0.5186 $\pm$ 0.0772    | 38.2339      | 42.9619  | 0.5351 $\pm$ 0.0772 | 0.4779    | 0.4779        | 0.4780          |
| 1    | 460             | 470     | 0.9787   | 0.0021  | 0.0489      | 0.0979          | 0.0734            | 0.5715 $\pm$ 0.0610 | 37.7297  | 42.5357  | 0.5225 $\pm$ 0.0610  | 41.2679    | 43.4146  | 0.547 $\pm$ 0.0610     | 39.4196      | 42.9619  | 0.6225 $\pm$ 0.0610 | 0.5579    | 0.5967        | 0.5774          |
| 2    | 244             | 470     | 0.2596   | 0.0021  | 0.0000      | 0.0003          | 0.0002            | 0.0879 $\pm$ 0.0036 | 130.1195 | 133.7755 | 0.0876 $\pm$ 0.0036  | 130.5651   | 134.3903 | 0.0877 $\pm$ 0.0036    | 130.4162     | 134.1423 | 0.0900 $\pm$ 0.0036 | 0.0876    | 0.0875        | 0.0876          |
| 2    | 312             | 470     | 0.3319   | 0.0021  | 0.0001      | 0.0005          | 0.0003            | 0.1052 $\pm$ 0.0103 | 139.0209 | 133.7755 | 0.1048 $\pm$ 0.0103  | 139.5515   | 134.3903 | 0.105 $\pm$ 0.0103     | 139.2857     | 134.1423 | 0.1074 $\pm$ 0.0103 | 0.1115    | 0.1114        | 0.1114          |
| 2    | 352             | 470     | 0.3745   | 0.0021  | 0.0001      | 0.0006          | 0.0004            | 0.1278 $\pm$ 0.0125 | 129.1080 | 133.7755 | 0.1273 $\pm$ 0.0125  | 129.6151   | 134.3903 | 0.1275 $\pm$ 0.0125    | 129.4118     | 134.1423 | 0.1300 $\pm$ 0.0125 | 0.1255    | 0.1255        | 0.1255          |
| 2    | 423             | 470     | 0.4500   | 0.0021  | 0.0002      | 0.0008          | 0.0006            | 0.1663 $\pm$ 0.0085 | 119.2311 | 133.7755 | 0.1657 $\pm$ 0.0085  | 119.6628   | 134.3903 | 0.1659 $\pm$ 0.0085    | 119.5185     | 134.1423 | 0.1686 $\pm$ 0.0085 | 0.1505    | 0.1504        | 0.1505          |
| 2    | 460             | 470     | 0.4894   | 0.0021  | 0.0003      | 0.0010          | 0.0007            | 0.1709 $\pm$ 0.0180 | 126.1703 | 133.7755 | 0.1702 $\pm$ 0.0180  | 126.6892   | 134.3903 | 0.1705 $\pm$ 0.0180    | 126.4663     | 134.1423 | 0.1733 $\pm$ 0.0180 | 0.1636    | 0.1635        | 0.1635          |
| 2    | 566             | 470     | 0.6021   | 0.0021  | 0.0006      | 0.0016          | 0.0012            | 0.1908 $\pm$ 0.0160 | 139.0527 | 133.7755 | 0.1898 $\pm$ 0.0160  | 139.7853   | 134.3903 | 0.1902 $\pm$ 0.0160    | 139.4913     | 134.1423 | 0.1935 $\pm$ 0.0160 | 0.2010    | 0.2011        | 0.2011          |
| 2    | 670             | 470     | 0.7128   | 0.0021  | 0.0011      | 0.0026          | 0.0020            | 0.2043 $\pm$ 0.0136 | 153.7261 | 133.7755 | 0.2028 $\pm$ 0.0136  | 154.8632   | 134.3903 | 0.2034 $\pm$ 0.0136    | 154.4063     | 134.1423 | 0.2075 $\pm$ 0.0136 | 0.2380    | 0.2384        | 0.2382          |
| 4    | 244             | 470     | 0.1298   | 0.0021  | 0.0000      | 0.0000          | 0.0000            | 0.0685 $\pm$ 0.0019 | 166.9708 | 226.2017 | 0.0685 $\pm$ 0.0019  | 166.9708   | 226.4957 | 0.0685 $\pm$ 0.0019    | 166.9708     | 226.3851 | 0.0706 $\pm$ 0.0019 | 0.0527    | 0.0526        | 0.0526          |
| 4    | 312             | 470     | 0.1660   | 0.0021  | 0.0000      | 0.0001          | 0.0000            | 0.0753 $\pm$ 0.0045 | 194.2231 | 226.2017 | 0.0752 $\pm$ 0.0045  | 194.4814   | 226.4957 | 0.0753 $\pm$ 0.0045    | 194.2231     | 226.3851 | 0.0774 $\pm$ 0.0045 | 0.0668    | 0.0668        | 0.0667          |
| 4    | 352             | 470     | 0.1872   | 0.0021  | 0.0000      | 0.0001          | 0.0000            | 0.0767 $\pm$ 0.0040 | 215.1239 | 226.2017 | 0.0766 $\pm$ 0.0040  | 215.4047   | 226.4957 | 0.0767 $\pm$ 0.0040    | 215.1239     | 226.3851 | 0.0788 $\pm$ 0.0040 | 0.0750    | 0.0750        | 0.0750          |
| 4    | 423             | 470     | 0.2250   | 0.0021  | 0.0000      | 0.0001          | 0.0001            | 0.0796 $\pm$ 0.0038 | 249.0970 | 226.2017 | 0.0795 $\pm$ 0.0038  | 249.4104   | 226.4957 | 0.0795 $\pm$ 0.0038    | 249.4104     | 226.3851 | 0.0817 $\pm$ 0.0038 | 0.0898    | 0.0897        | 0.0898          |
| 4    | 460             | 470     | 0.2447   | 0.0021  | 0.0000      | 0.0001          | 0.0001            | 0.0922 $\pm$ 0.0060 | 233.8666 | 226.2017 | 0.0921 $\pm$ 0.0060  | 234.1205   | 226.4957 | 0.0921 $\pm$ 0.0060    | 234.1205     | 226.3851 | 0.0943 $\pm$ 0.0060 | 0.0974    | 0.0974        | 0.0974          |
| 4    | 566             | 470     | 0.3011   | 0.0021  | 0.0000      | 0.0002          | 0.0001            | 0.1065 $\pm$ 0.0030 | 249.1197 | 226.2017 | 0.1063 $\pm$ 0.0030  | 249.5884   | 226.4957 | 0.1064 $\pm$ 0.0030    | 249.3539     | 226.3851 | 0.1086 $\pm$ 0.0030 | 0.1194    | 0.1194        | 0.1194          |
| 4    | 670             | 470     | 0.3564   | 0.0021  | 0.0000      | 0.0002          | 0.0002            | 0.1142 $\pm$ 0.0090 | 275.0109 | 226.2017 | 0.114 $\pm$ 0.0090   | 275.4934   | 226.4957 | 0.114 $\pm$ 0.0090     | 275.4934     | 226.3851 | 0.1163 $\pm$ 0.0090 | 0.1409    | 0.1410        | 0.1410          |

Table 2 shows the throughput and latency of an endorsing peer with $c=1, 2, 4$ CPU core(s) in cluster 2. It validates the performance mode of throughput and latency in the execute phase. The details of performance metrics are as follows:

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
      <li> Example 1: The maximum throughput of an endorsing peer with a single CPU core, i.e., $c=1$, is $\mu^e=470$ transactions per second.</li>
    </ul>
  </li>

  <li> Performance metric - $\rho^e$
    <ul>
      <li> Explanation: The utilization of an endorsing peer in the execute phase, where we can derive $\rho^e=\lambda^e/(c\mu^e)$.</li>
      <li> Example 1: The maximum throughput of an endorsing peer with a single CPU core, i.e., $c=1$, is $\mu^e=470$ transactions per second,  $\lambda^e=214$ transactions per second, and hence $\rho^e=\lambda^e/(c\mu^e)=214/(1*470)=0.4553$.</li>
    </ul>
  </li>

  <li> Performance metric - $T_s^e$
    <ul>
      <li> Explanation: The service time of a transaction in the execute phase, where we can derive $T_s^e=1/ \mu^e$.</li>
      <li> Example 1: The service time of a transaction in the execute phase, where we can derive $T_s^e=1/ \mu^e=1/470=0.0021$ seconds.</li>
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
      <li> Example 1: The number of CPU cores $c=1$ and the transaction arrival rate $\lambda^e=214$ transactions per second. We then have the queueing latency $T_q^e=0.0009$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.2155$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.2125$ seconds. And when $c=1$, the average effective network bandwidth is stable around $\beta^e=42.5357$ Mbps, from which the model has an overall latency $T^e=0.2388$ seconds.</li>
      <li> Example 2: The number of CPU cores be $c=2$ and the transaction arrival rate be $\lambda^e=244$ transactions per second; we have the queueing latency $T_q^e=0.0000$ seconds. We measure the overall latency of a transaction spent in the execute phase $T^e=0.0900$ seconds, from which the communication latency of a transaction spent in the execute phase $T_{comm}^e=0.0879$ seconds. And when $c=2$, the average effective network bandwidth is stable around $\beta^e=133.7755$ Mbps, from which the model has an overall latency $T^e=0.0876$ seconds.</li>
    </ul>
  </li>

</ul>



#### 4.3. Order Phase with a BatchSize of 20 in Cluster 1

Table 3. The effects of OSNs on the throughput and latency in the order phase. There are $k=$3,9,15 OSNs in cluster 1 of 1 Gbit/s Ethernet network. The BatchSize is 20 and the BatchTimeout is 1.

|      | Measure derived |         |          |         |              | Measure             |          |         |                     |          |          |                     |            |          |                     |                 |                     | Our model |               |
| ---- | --------------- | ------- | -------- | ------- | ------------ | ------------------- | -------- | ------- | ------------------- | -------- | -------- | ------------------- | ---------- | -------- | ------------------- | --------------- | ------------------- | --------- | ------------- |
| $k$  | $\lambda^r$     | $\mu^r$ | $\rho^r$ | $T_s^r$ | $T_{w}^r$ | $T_{c2l}^r$         | BW       | avg BW  | Our $T_{l2f}^r$     | Our BW   | avg BW   | $M/M/1$ $T_{l2f}^r$ | $M/M/1$ BW | avg BW   | Our $T_q^r$         | $M/M/1$ $T_q^r$ | $T^r$               | Our $T^r$ | $M/M/1$ $T^r$ |
| 3    | 70              | 190     | 0.3684   | 0.0053  | 0.1429       | 0.0403 $\pm$ 0.0061 | 40.7103  | 55.1617 | 0.1928 $\pm$ 0.1082 | 17.0189  | 17.4942  | 0.1901 $\pm$ 0.1082 | 17.2607    | 17.7970  | 0.0004 $\pm$ 0.0008 | 0.0031          | 0.3817 $\pm$ 0.1051 | 0.3659    | 0.2225        |
| 3    | 109             | 190     | 0.5737   | 0.0053  | 0.0917       | 0.0521 $\pm$ 0.0080 | 49.0343  | 55.1617 | 0.2818 $\pm$ 0.0705 | 18.1312  | 17.4942  | 0.277 $\pm$ 0.0705  | 18.4454    | 17.7970  | 0.0023 $\pm$ 0.0010 | 0.0071          | 0.4332 $\pm$ 0.0792 | 0.4377    | 0.3458        |
| 3    | 180             | 190     | 0.9474   | 0.0053  | 0.0556       | 0.0557 $\pm$ 0.0160 | 75.7406  | 55.1617 | 0.4868 $\pm$ 0.1246 | 17.3326  | 17.4942  | 0.4771 $\pm$ 0.1246 | 17.6850    | 17.7970  | 0.0850 $\pm$ 0.0013 | 0.0947          | 0.6884 $\pm$ 0.1411 | 0.7047    | 0.6506        |
| 9    | 70              | 190     | 0.3684   | 0.0053  | 0.1429       | 0.0422 $\pm$ 0.0061 | 38.8774  | 64.9560 | 0.2395 $\pm$ 0.0628 | 54.8017  | 50.8648  | 0.2368 $\pm$ 0.0628 | 55.4265    | 51.4904  | 0.0004 $\pm$ 0.0000 | 0.0031          | 0.4303 $\pm$ 0.0636 | 0.4319    | 0.2886        |
| 9    | 109             | 190     | 0.5737   | 0.0053  | 0.0917       | 0.0466 $\pm$ 0.0047 | 54.8216  | 64.9560 | 0.382 $\pm$ 0.1053  | 53.5013  | 50.8648  | 0.3772 $\pm$ 0.1053 | 54.1821    | 51.4904  | 0.0023 $\pm$ 0.0004 | 0.0071          | 0.5279 $\pm$ 0.1083 | 0.5404    | 0.4486        |
| 9    | 180             | 190     | 0.9474   | 0.0053  | 0.0556       | 0.0417 $\pm$ 0.0050 | 101.1691 | 64.9560 | 0.762 $\pm$ 0.1476  | 44.2913  | 50.8648  | 0.7523 $\pm$ 0.1476 | 44.8624    | 51.4904  | 0.0850 $\pm$ 0.0131 | 0.0947          | 0.9496 $\pm$ 0.1345 | 0.8744    | 0.8204        |
| 15   | 70              | 190     | 0.3684   | 0.0053  | 0.1429       | 0.0522 $\pm$ 0.0163 | 31.4296  | 52.4210 | 0.2191 $\pm$ 0.0582 | 104.8323 | 106.4712 | 0.2164 $\pm$ 0.0582 | 106.1402   | 108.0775 | 0.0004 $\pm$ 0.0006 | 0.0031          | 0.4199 $\pm$ 0.0466 | 0.3956    | 0.2522        |
| 15   | 109             | 190     | 0.5737   | 0.0053  | 0.0917       | 0.0549 $\pm$ 0.0136 | 46.5335  | 52.4210 | 0.2722 $\pm$ 0.0478 | 131.3947 | 106.4712 | 0.2674 $\pm$ 0.0478 | 133.7533   | 108.0775 | 0.0023 $\pm$ 0.0011 | 0.0071          | 0.4264 $\pm$ 0.0589 | 0.4840    | 0.3921        |
| 15   | 180             | 190     | 0.9474   | 0.0053  | 0.0556       | 0.0532 $\pm$ 0.0136 | 79.2998  | 52.4210 | 0.71 $\pm$ 0.1740   | 83.1866  | 106.4712 | 0.7003 $\pm$ 0.1740 | 84.3389    | 108.0775 | 0.0850 $\pm$ 0.0155 | 0.0947          | 0.9091 $\pm$ 0.1467 | 0.7811    | 0.7270        |

Table 3 shows the effects of OSNs on throughput and latency during the order phase. There are $k=3, 9, 15$ OSNs in cluster 1 of a 1 Gbit/s Ethernet network. The \textit{BatchSize} is 20 and the \textit{BatchTimeout} is 1. It validates the model of throughput and latency in the order phase. The details of performance metrics are as follows:

<ul>

  <li> Performance metric - $k$
    <ul>
      <li> Explanation: The number of ordering service nodes in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\lambda^r$
    <ul>
      <li> Explanation: The transaction arrival rate in transactions per second in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\mu^r$
    <ul>
      <li> Explanation: The maximum throughput of the ordering service in the order phase.</li>
      <li> Example 1: The maximum throughput of the ordering service with three ordering service nodes, i.e., $k=3$, is $\mu^r=190$ transactions per second.</li>
    </ul>
  </li>

  <li> Performance metric - $\rho^r$
    <ul>
      <li> Explanation: The utilization of the ordering service in the order phase, where we can derive $\rho^r=\lambda^r/ \mu^r$.</li>
      <li> Example 1: The maximum throughput of the ordering service with three ordering service nodes is $\mu^r=190$ transactions per second, $\lambda^r=70$ transactions per second, and hence $\rho^r=\lambda^r/ \mu^r=70/190=0.3684$.</li>
    </ul>
  </li>

  <li> Performance metric - $T_s^r$
    <ul>
      <li> Explanation: The service time of a transaction in the order phase, where we can derive $T_s^r=1/ \mu^r$.</li>
      <li> Example 1: The service time of a transaction in the order phase, where we can derive $T_s^r=1/ \mu^r=1/190=0.0053$ seconds.</li>
    </ul>
  </li>

  <li> Performance metric - $T_q^r$
    <ul>
      <li> Explanation: The queueing latency of a transaction in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $T_w^r$
    <ul>
      <li> Explanation: The waiting time of a transaction in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $T_{c2l}^r$, $T_{l2f}^r$
    <ul>
      <li> Explanation: The communication latency spent between the client and the ordering service.</li>
      <li> Example 1: The number of ordering service nodes be $k=3$ and the transaction arrival rate be $\lambda^r=70$ transactions per second, we have a queueing latency of $T_q^r=0.0004$ seconds. We measure the overall latency of a transaction spent in the order phase $T^r=0.3817$ seconds and the communication latency spent between the client and the ordering service $T_{c2l}^r=0.0403$ seconds, from which the communication latency spent between the OSN leader and followers $T_{l2f}^r=0.1928$. And when $k=3$, the effective network bandwidth is stable around $\beta_{c2l}^r=55.1617$ Mbps, $\beta_{l2f}^r=17.4942$ Mbps, from which the model has an overall latency $T^r=0.3659$ seconds.</li>
    </ul>
  </li>

</ul>


#### 4.4. Order Phase with a BatchSize of 50 in Cluster 1

Table 4. The effects of OSNs on the throughput and latency in the order phase. There are $k=$3,9,15 OSNs in cluster 1 of 1 Gbit/s Ethernet network. The BatchSize is 50 and the BatchTimeout is 1.

|      | Measure derived |         |          |         |           | Measure             |          |          |                     |          |          |                     |            |          |                     |                   |                     | Our model |               |
| ---- | --------------- | ------- | -------- | ------- | --------- | ------------------- | -------- | -------- | ------------------- | -------- | -------- | ------------------- | ---------- | -------- | ------------------- | ----------------- | ------------------- | --------- | ------------- |
| $k$  | $\lambda^r$     | $\mu^r$ | $\rho^r$ | $T_s^r$ | $T_{w}^r$ | $T_{c2l}^r$         | BW       | avg BW   | Our $T_{l2f}^r$     | Our BW   | avg BW   | $M/M/1$ $T_{l2f}^r$ | $M/M/1$ BW | avg BW   | Our $T_{q}^r$       | $M/M/1$ $T_{q}^r$ | $T^r$               | Our $T^r$ | $M/M/1$ $T^r$ |
| 3    | 109             | 370     | 0.2946   | 0.0027  | 0.2294    | 0.0516 $\pm$ 0.0150 | 49.5094  | 117.2577 | 0.0987 $\pm$ 0.0444 | 51.7667  | 52.9649  | 0.0976 $\pm$ 0.0444 | 52.3502    | 53.7112  | 0.0000 $\pm$ 0.0000 | 0.0011            | 0.3824 $\pm$ 0.0481 | 0.3504    | 0.1207        |
| 3    | 180             | 370     | 0.4865   | 0.0027  | 0.1389    | 0.0552 $\pm$ 0.0059 | 76.4266  | 117.2577 | 0.1648 $\pm$ 0.0330 | 51.1984  | 52.9649  | 0.1628 $\pm$ 0.0330 | 51.8274    | 53.7112  | 0.0006 $\pm$ 0.0001 | 0.0026            | 0.3622 $\pm$ 0.0346 | 0.3375    | 0.1984        |
| 3    | 263             | 370     | 0.7108   | 0.0027  | 0.0951    | 0.0539 $\pm$ 0.0104 | 114.3611 | 117.2577 | 0.1929 $\pm$ 0.0464 | 63.9094  | 52.9649  | 0.1897 $\pm$ 0.0464 | 64.9875    | 53.7112  | 0.0034 $\pm$ 0.0004 | 0.0066            | 0.3480 $\pm$ 0.0473 | 0.3865    | 0.2914        |
| 3    | 310             | 370     | 0.8378   | 0.0027  | 0.0806    | 0.0424 $\pm$ 0.0045 | 171.3591 | 117.2577 | 0.316 $\pm$ 0.1288  | 45.9850  | 52.9649  | 0.3118 $\pm$ 0.1288 | 46.6044    | 53.7112  | 0.0098 $\pm$ 0.0005 | 0.0140            | 0.4515 $\pm$ 0.1325 | 0.4294    | 0.3492        |
| 3    | 342             | 370     | 0.9243   | 0.0027  | 0.0731    | 0.0459 $\pm$ 0.0059 | 174.6324 | 117.2577 | 0.3085 $\pm$ 0.1071 | 51.9652  | 52.9649  | 0.3037 $\pm$ 0.1071 | 52.7865    | 53.7112  | 0.0282 $\pm$ 0.0012 | 0.0330            | 0.4584 $\pm$ 0.1088 | 0.4750    | 0.4025        |
| 9    | 109             | 370     | 0.2946   | 0.0027  | 0.2294    | 0.0552 $\pm$ 0.0148 | 46.2806  | 112.7968 | 0.1385 $\pm$ 0.0743 | 147.5632 | 181.2399 | 0.1374 $\pm$ 0.0743 | 148.7445   | 183.4481 | 0.0000 $\pm$ 0.0001 | 0.0011            | 0.4258 $\pm$ 0.0666 | 0.3675    | 0.1379        |
| 9    | 180             | 370     | 0.4865   | 0.0027  | 0.1389    | 0.0584 $\pm$ 0.0161 | 72.2389  | 112.7968 | 0.1719 $\pm$ 0.0298 | 196.3351 | 181.2399 | 0.1699 $\pm$ 0.0298 | 198.6463   | 183.4481 | 0.0006 $\pm$ 0.0000 | 0.0026            | 0.3725 $\pm$ 0.0433 | 0.3658    | 0.2267        |
| 9    | 263             | 370     | 0.7108   | 0.0027  | 0.0951    | 0.0569 $\pm$ 0.0139 | 108.3315 | 112.7968 | 0.2588 $\pm$ 0.0489 | 190.5429 | 181.2399 | 0.2556 $\pm$ 0.0489 | 192.9284   | 183.4481 | 0.0034 $\pm$ 0.0001 | 0.0066            | 0.4169 $\pm$ 0.0367 | 0.4279    | 0.3328        |
| 9    | 310             | 370     | 0.8378   | 0.0027  | 0.0806    | 0.0443 $\pm$ 0.0051 | 164.0096 | 112.7968 | 0.3219 $\pm$ 0.0684 | 180.5685 | 181.2399 | 0.3177 $\pm$ 0.0684 | 182.9556   | 183.4481 | 0.0098 $\pm$ 0.0001 | 0.0140            | 0.4593 $\pm$ 0.0660 | 0.4782    | 0.3980        |
| 9    | 342             | 370     | 0.9243   | 0.0027  | 0.0731    | 0.0463 $\pm$ 0.0053 | 173.1237 | 112.7968 | 0.3354 $\pm$ 0.1094 | 191.1896 | 181.2399 | 0.3306 $\pm$ 0.1094 | 193.9655   | 183.4481 | 0.0282 $\pm$ 0.0003 | 0.0330            | 0.4857 $\pm$ 0.1046 | 0.5289    | 0.4563        |
| 15   | 109             | 370     | 0.2946   | 0.0027  | 0.2294    | 0.0397 $\pm$ 0.0055 | 64.3498  | 144.4729 | 0.1512 $\pm$ 0.0274 | 236.5451 | 308.0953 | 0.1501 $\pm$ 0.0274 | 238.2786   | 311.8089 | 0.0000 $\pm$ 0.0001 | 0.0011            | 0.4230 $\pm$ 0.0281 | 0.3659    | 0.1362        |
| 15   | 180             | 370     | 0.4865   | 0.0027  | 0.1389    | 0.0439 $\pm$ 0.0093 | 96.0991  | 144.4729 | 0.1955 $\pm$ 0.0141 | 302.1100 | 308.0953 | 0.1935 $\pm$ 0.0141 | 305.2326   | 311.8089 | 0.0006 $\pm$ 0.0000 | 0.0026            | 0.3816 $\pm$ 0.0154 | 0.3631    | 0.2239        |
| 15   | 263             | 370     | 0.7108   | 0.0027  | 0.0951    | 0.0363 $\pm$ 0.0049 | 169.8089 | 144.4729 | 0.2394 $\pm$ 0.0263 | 360.4715 | 308.0953 | 0.2362 $\pm$ 0.0263 | 365.3551   | 311.8089 | 0.0034 $\pm$ 0.0001 | 0.0066            | 0.3769 $\pm$ 0.0294 | 0.4240    | 0.3287        |
| 15   | 310             | 370     | 0.8378   | 0.0027  | 0.0806    | 0.0410 $\pm$ 0.0044 | 177.2104 | 144.4729 | 0.3409 $\pm$ 0.0448 | 298.3830 | 308.0953 | 0.3367 $\pm$ 0.0448 | 302.1050   | 311.8089 | 0.0098 $\pm$ 0.0000 | 0.0140            | 0.4750 $\pm$ 0.0480 | 0.4735    | 0.3932        |
| 15   | 342             | 370     | 0.9243   | 0.0027  | 0.0731    | 0.0373 $\pm$ 0.0037 | 214.8961 | 144.4729 | 0.3272 $\pm$ 0.0713 | 342.9668 | 308.0953 | 0.3224 $\pm$ 0.0713 | 348.0730   | 311.8089 | 0.0282 $\pm$ 0.0008 | 0.0330            | 0.4685 $\pm$ 0.0711 | 0.5237    | 0.4511        |

Table 4 shows the effects of OSNs on throughput and latency during the order phase. There are $k=3, 9, 15$ OSNs in cluster 1 of a 1 Gbit/s Ethernet network. The \textit{BatchSize} is 50 and the \textit{BatchTimeout} is 1. It validates the model of throughput and latency in the order phase. The details of performance metrics are as follows:

<ul>


  <li> Performance metric - $k$
    <ul>
      <li> Explanation: The number of ordering service nodes in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\lambda^r$
    <ul>
      <li> Explanation: The transaction arrival rate in transactions per second in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $\mu^r$
    <ul>
      <li> Explanation: The maximum throughput of the ordering service in the order phase.</li>
      <li> Example 1: The maximum throughput of the ordering service with three ordering service nodes, i.e., $k=3$, is $\mu^r=370$ transactions per second.</li>
    </ul>
  </li>

  <li> Performance metric - $\rho^r$
    <ul>
      <li> Explanation: The utilization of the ordering service in the order phase, where we can derive $\rho^r=\lambda^r/ \mu^r$.</li>
      <li> Example 1: The maximum throughput of the ordering service with three ordering service nodes is $\mu^r=370$ transactions per second, $\lambda^r=109$ transactions per second, and hence $\rho^r=\lambda^r/ \mu^r=109/370=0.2946$.</li>
    </ul>
  </li>

  <li> Performance metric - $T_s^r$
    <ul>
      <li> Explanation: The service time of a transaction in the order phase, where we can derive $T_s^r=1/ \mu^r$.</li>
      <li> Example 1: The service time of a transaction in the order phase, where we can derive $T_s^r=1/ \mu^r=1/370=0.0027$ seconds.</li>
    </ul>
  </li>

  <li> Performance metric - $T_q^r$
    <ul>
      <li> Explanation: The queueing latency of a transaction in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $T_w^r$
    <ul>
      <li> Explanation: The waiting time of a transaction in the order phase.</li>
    </ul>
  </li>

  <li> Performance metric - $T_{c2l}^r$, $T_{l2f}^r$
    <ul>
      <li> Explanation: The communication latency spent between the client and the ordering service.</li>
      <li> Example 1: The number of ordering service nodes is $k=3$ and the transaction arrival rate is $\lambda^r=109$ transactions per second, we have a queueing latency of $T_q^r=0.0000$ seconds. We measure the overall latency of a transaction spent in the order phase $T^r=0.3824$ seconds and the communication latency spent between the client and the ordering service $T_{c2l}^r=0.0516$ seconds, from which the communication latency spent between the OSN leader and followers $T_{l2f}^r=0.0987$. And when $k=3$, the effective network bandwidth is stable around $\beta_{c2l}^r=117.2577$ Mbps, $\beta_{l2f}^r=52.9649$~Mbps, from which the model has an overall latency $T^r=0.3504$~seconds.</li>
    </ul>
  </li>

</ul>


#### 4.5. Order Phase with a BatchSize of 2 in Cluster 2

Table 5. The effects of OSNs on the throughput and latency in the order phase. There are $k=$3,9,15 OSNs in cluster 2 of 10 Gbit/s Ethernet network. The BatchSize is 2 and the BatchTimeout is 1.


























## License

Hyperledger_Fabric_Phase_Bench source code is available under the MIT License 2026.


## Reference
[1. Hyperledger Fabric] https://github.com/hyperledger/fabric/tree/v2.2.0 <br>
[2. Hyperledger Fabric Dynamic Channel Update] https://hyperledger-fabric.readthedocs.io/en/release-2.2/config_update.html <br>
[3. Hyperledger Fabric SDK for node.js] https://hyperledger.github.io/fabric-sdk-node/release-1.4/module-fabric-network.html
