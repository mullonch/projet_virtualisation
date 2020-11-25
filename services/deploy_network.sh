#!/bin/bash
while [ $# -gt 0 ]; do
   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
   fi
  shift
done
echo "Déploiement du réseau (id = $id ; adress = $address)"
neutron net-create $id
neutron subnet-create $id $address --name sub$id
echo "Réseau déployé."