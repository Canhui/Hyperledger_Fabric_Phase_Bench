/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
'use strict';
const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
var tlscfgname = '/root/fabric-samples/demo-first/workload/tls/connection-peer0-org2.json'
var channelname = 'mychannel'
var userid = 'User1@org2.example.com'
var chaincodename = 'mycc'
async function main() {
    try {
        // load the network configuration
        const ccp = JSON.parse(fs.readFileSync(tlscfgname, 'utf8'));
        // Create a new file system based wallet for managing identities.
        const walletPath = path.join('/root/fabric-samples/demo-first/workload', 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        //console.log(`Wallet path: ${walletPath}`);
        console.log('wallet:', wallet);
        // Check to see if we've already enrolled the user.
        const identity = await wallet.get(userid);
        if (!identity) {
            console.log('An identity for the user "user1.id" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: userid, discovery: { enabled: true, asLocalhost: false } });
        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork(channelname);
        // Get the contract from the network.
        const contract = network.getContract(chaincodename);
        // Evaluate the specified transaction.
        // queryCar transaction - requires 1 argument, ex: ('queryCar', 'CAR4')
        // queryAllCars transaction - requires no arguments, ex: ('queryAllCars')
        const result = await contract.evaluateTransaction('query', 'a');
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);
        // Disconnect from the gateway.
        await gateway.disconnect();
        
    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
}
main();
