#!/bin/bash
#LINE=$(ip address | grep '\eth0$')
#ADDRESS=$(echo $LINE | grep -o '[0-9]\{0,3\}\.[0-9]\{0,3\}\.[0-9]\{0,3\}\.[0-9]\{0,3\}')

sed -i "s/host=\".*\"/host=\"0.0.0.0\"/g" swagger_server/__main__.py
sed -i "s/port=[0-9][0-9][0-9][0-9]/port=8080/g" swagger_server/__main__.py
#sed -i "s/host: \".*\"/host: \"${ADDRESS}:8080\"/g" swagger_server/swagger/swagger.yaml
