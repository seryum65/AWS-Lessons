#!/bin/bash
apt-get update -y
apt-get install git -y
apt-get install python3 -y
cd /home/ubuntu/
TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
git clone https://$TOKEN@github.com/seryum65/seryum_aws_capstone_project.git
cd /home/ubuntu/seryum_aws_capstone_project
apt install python3-pip -y
apt-get install python3.7-dev libmysqlclient-dev -y
pip3 install -r requirements.txt
cd /home/ubuntu/seryum_aws_capstone_project/src
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80

