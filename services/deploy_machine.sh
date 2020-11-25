#!/bin/bash
while [ $# -gt 0 ]; do
   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
   fi
  shift
done
echo "Déploiement de la machine (id = $id ; image = $image ; in_network = $in_network)"
nova boot --flavor small2 --image $image --nic net-name=$in_network $id