#!/bin/bash
echo "Vérification de l'installation du client openstack..."
REQUIRED_PKG="python3-openstackclient"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "Client Openstack non installé, début de l'installation..."
  sudo apt-get --yes install $REQUIRED_PKG 
fi
echo "Client openstack ok !"
source Openstack_configuration/VLDM1-openrc.sh
echo "Configuration ok !";