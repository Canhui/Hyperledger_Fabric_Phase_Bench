#--------------------------------------------------------------------------------------------------
# Copy workload file
#--------------------------------------------------------------------------------------------------
# The workload file
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.70:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.71:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.77:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.78:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.79:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.132:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.134:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.138:$HOME/fabric-samples/demo-first/workload
# scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.71:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.153:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.154:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.155:$HOME/fabric-samples/demo-first/workload
#scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@192.168.0.156:$HOME/fabric-samples/demo-first/workload
