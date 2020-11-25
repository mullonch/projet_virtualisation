#!/bin/bash
while [ $# -gt 0 ]; do
   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
   fi
  shift
done
echo "Association de l'interface du routeur $router_id vers le réseau $nw_id (adresse : $address)"
portId=$(neutron port-create $nw_id --fixed-ip ip_address=$address | grep " id " | cut -c27-62)
neutron router-interface-add $router_id port=$portId