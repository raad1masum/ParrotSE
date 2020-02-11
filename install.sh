#!/bin/bash

apt-get -y update
apt-get -y install software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get -y update
apt-get -y install python3.6
apt-get -y install python3-pip
apt-get -y install python3-setuptools