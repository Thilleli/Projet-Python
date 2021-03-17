#!/bin/bash

if [ "$#" -ne 3 ]
then
    echo "Le nombre d'arguments est invalide."
    echo "Il doit y avoir *nom_cvs* *nom_txt* *nom_html*"
    exit 1
fi

python ../Projet/analyse.py $1 $2 $3
