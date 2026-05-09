# Project under the directory of $HOME/fabric-samples
project="demo-first"
channel="mychannel"

# Use the cryptogen to generate certificates
cd $HOME/fabric-samples/$project
../bin/cryptogen generate --config=./crypto-config.yaml

# Use configtxgen to generate the genesis block
cd $HOME/fabric-samples/demo-first
mkdir channel-artifacts
export FABRIC_CFG_PATH=$PWD
../bin/configtxgen -profile SampleMultiNodeEtcdRaft -channelID byfn-sys-channel -outputBlock ./channel-artifacts/genesis.block

# Use configtxgen to generate configuration transaction
export CHANNEL_NAME=$channel
../bin/configtxgen -profile TwoOrgsChannel -outputCreateChannelTx ./channel-artifacts/channel.tx -channelID $CHANNEL_NAME

# Define anchor peers
../bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/Org1MSPanchors.tx -channelID $CHANNEL_NAME -asOrg Org1MSP
../bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/Org2MSPanchors.tx -channelID $CHANNEL_NAME -asOrg Org2MSP


# Start the docker network
#export COMPOSE_PROJECT_NAME=net
#export SYS_CHANNEL=byfn-sys-channel
#export IMAGE_TAG=2.2.0
#docker-compose -f orderer1-152.yaml up -d
#docker-compose -f docker-compose-cli.yaml -f docker-compose-etcdraft2.yaml up -d

# ---------------------------------------------------------------------------------------------
# chaincode directory
# chaincodepath="/home/t716/fabric-samples/chaincode/abstore/go/"
# chaincodepath="github.com/hyperledger/fabric-samples/chaincode/abstore/go/"
# cd /opt/gopath/src/$chaincodepath
# cd $chaincodepath
# GO111MODULE=on go mod vendor
