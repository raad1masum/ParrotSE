#!/bin/bash

apt-get -y update
apt-get -y install software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get -y update
apt-get -y install python3.6
apt-get -y install python3-pip
apt-get -y install python3-setuptools

echo '* * * * * root /usr/local/bin/score' >> /etc/crontab
echo 'ALL ALL=NOPASSWD: /usr/local/bin/score' > /etc/sudoers.d/ScoreEngine
chattr +i /etc/sudoers.d/ScoreEngine
echo "/usr/lib/notify-osd/notify-osd &" >> /etc/profile

echo "
#!/bin/bash
python3 ParrotSE.py" > /usr/local/bin/score

chown root:root /usr/local/bin/score
chmod 4755 /usr/local/bin/score
chattr +i /usr/local/bin/score

cp report.desktop /home/*/Desktop
chmod 777 /home/*/Desktop/report.desktop
