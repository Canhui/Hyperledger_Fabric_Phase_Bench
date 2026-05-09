tlscfgname="$HOME/fabric-samples/demo-first/workload/tls/connection-peer0-org1.json"
userid='User1@org1.example.com'
invokefile='sdk-peer0-org1/invoke.js'
queryfile='sdk-peer0-org1/query.js'
walletpath="$HOME/fabric-samples/demo-first/workload"

# details
cat>$HOME/fabric-samples/demo-first/workload/$invokefile<<EOF
'use strict';

// -----------------------------------------------
// Dependencies
// -----------------------------------------------
const {Gateway, Wallets, DefaultEventHandlerStrategies} = require('fabric-network');
const fs = require('fs');
const path = require('path');
//import { DefaultEventHandlerStrategies } from 'fabric-network';

// -----------------------------------------------
// Settings
// -----------------------------------------------
var tlscfgname = '$tlscfgname'
var channelname = 'mychannel'
var userid = '$userid'
var chaincodename = 'mycc'

// -----------------------------------------------
// Global Handlers
// -----------------------------------------------
// load the network configuration
var ccp;
var gateway;
var contract;
var rounds = process.argv[4];

// -----------------------------------------------
// Load Settings/wallet <------- Only one load, Multi txs
// -----------------------------------------------
async function setting(){
	// create a wallet
	ccp = JSON.parse(fs.readFileSync(tlscfgname, 'utf8'));
	const walletPath = path.join('$walletpath', 'wallet');
	const wallet = await Wallets.newFileSystemWallet(walletPath);
	console.log(\`Wallet path: \${walletPath}\`);
	// check whether wallet user is valid
	const identity = await wallet.get(userid);
	if (!identity) {
        console.log('An identity for the user "appUser" does not exist in the wallet');
        console.log('Run the registerUser.js application before retrying');
        return;
    }
    // create a gateway for connecting to our peers
    gateway = new Gateway();
	await gateway.connect(ccp, 
            { wallet, 
              identity: userid, 
              discovery: { enabled: true, asLocalhost: false },
              eventHandlerOptions: {
                  strategy: DefaultEventHandlerStrategies.MSPID_SCOPE_ALLFORTX
                  //strategy: null
              }
            });
	// get our channel
	const network = await gateway.getNetwork(channelname);
	// get our contract
	contract = network.getContract(chaincodename);
    // add an event to the contract
    //contract.addContractListener(async (event) => {
    //    console.log(event.eventName, event.payload.toString("utf-8"));
    //});
}

async function app() {
    await setting();
    workload_controller();
    // console.log('2');
}

app()

// generate the payoff part of a transaction
function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

// -----------------------------------------------
// After load, submit a transaction
// -----------------------------------------------
function submit_a_tx_after_the_setting(){
    var t1 = Date.now()/1000;
    //console.log('Send_Endorsing_Proposal: %j', t1);
	//contract.submitTransaction('invoke', 'a', '330dota');
    contract.submitTransaction('invoke', 'a', makeid(process.argv[5]));
    //var t2 = Date.now()/1000;
    //console.log('Get_Endorsed_Proposal: %j', t2);
	//console.log("This transaction Finished on: ", new Date, "\n")
}

function workload(transactions){
    try{
        for(var i = 0; i < transactions; i++){
            submit_a_tx_after_the_setting();
        }
    } catch(e){}
}

function call(callback){
    workload(process.argv[2]); 
    callback();
}

// 30 tasks per batch
// 1 batch per round
// 500 ms delay per round, follows an exponential distribution
// 100 rounds in total
function workload_controller(){
    rounds--;
    if(rounds >= 0){
        //setTimeout(call, expDist(0.002), workload_controller);
        setTimeout(call, expDist(process.argv[3]), workload_controller);
    }
}
// The average delay is 1/lambda xxx
// The average delay is lambda yyy
function expDist(lambda){
    var p = Math.random(); // p is in [0, 1)
    //return (-1 / lambda) * Math.log(1 - p);
    return (-1 * lambda) * Math.log(1 - p);
}
EOF


cat>$HOME/fabric-samples/demo-first/workload/$queryfile<<EOF
/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
'use strict';
const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
var tlscfgname = '$tlscfgname'
var channelname = 'mychannel'
var userid = '$userid'
var chaincodename = 'mycc'
async function main() {
    try {
        // load the network configuration
        const ccp = JSON.parse(fs.readFileSync(tlscfgname, 'utf8'));
        // Create a new file system based wallet for managing identities.
        const walletPath = path.join('$walletpath', 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        //console.log(\`Wallet path: \${walletPath}\`);
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
        console.log(\`Transaction has been evaluated, result is: \${result.toString()}\`);
        // Disconnect from the gateway.
        await gateway.disconnect();
        
    } catch (error) {
        console.error(\`Failed to evaluate transaction: \${error}\`);
        process.exit(1);
    }
}
main();
EOF
