#!/bin/bash
while [ $# -gt 0 ]; do
   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
   fi
  shift
done
echo "Déploiement du routeur (id = $id)"
neutron router-create $id