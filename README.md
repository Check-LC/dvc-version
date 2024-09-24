#install dvc on ubuntu

sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list

wget -qO - https://dvc.org/deb/iterative.asc | gpg --dearmor > packages.iterative.gpg

sudo install -o root -g root -m 644 packages.iterative.gpg /etc/apt/trusted.gpg.d/

rm -f packages.iterative.gpg

sudo apt update

sudo apt install dvc

# 在目标路径下init （git init / dvc init ）

# 增加远程存储的配置

# dvc 添加到暂存区、push

# git 管理 dvc 的数据版本

# dvc client pull并使用数据

# 数据修改后的步骤放到了crontab.sh, 每天凌晨3点执行脚本
