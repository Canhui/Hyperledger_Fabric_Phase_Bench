#--------------------------------------------------------------------------------------------------
# Copy workload file
#--------------------------------------------------------------------------------------------------
# The workload file
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.70:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.71:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.77:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.78:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.79:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.80:$HOME/fabric-samples/demo-first/workload
scp -r `ls $HOME/fabric-samples/demo-first/workload | grep -v node_modules | xargs` $USER@172.31.210.81:$HOME/fabric-samples/demo-first/workload

