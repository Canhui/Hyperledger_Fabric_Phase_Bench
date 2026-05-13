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

This is the numerical results of the cluster 1
















<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
  <li>Fourth item</li>
</ul>

<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item
    <ul>
      <li>Indented item</li>
      <li>Indented item</li>
    </ul>
  </li>
  <li>Fourth item</li>
</ul>







## License

Fabric_Phase_Bench source code is available under the MIT License.


## Reference
[1. Hyperledger Fabric] https://github.com/hyperledger/fabric/tree/v2.2.0 <br>
[2. Hyperledger Fabric Dynamic Channel Update] https://hyperledger-fabric.readthedocs.io/en/release-2.2/config_update.html <br>
[3. Hyperledger Fabric SDK for node.js] https://hyperledger.github.io/fabric-sdk-node/release-1.4/module-fabric-network.html
