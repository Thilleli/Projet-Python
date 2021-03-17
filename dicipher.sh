#!/bin/bash

if [ -e $1 ]

then

    if [ -z $2 ]
    then
        python ../Projet/dicipher.py $1 "None"

    else
        if [ -e $2 ]
        then 
            echo "Voulez-vous écraser le fichier? (y/n): "
            read answer
            
            case $answer in
                y|Y)
                    python ../Projet/dicipher.py $1 $2
                    ;;
                n|N)
                    echo "L'ecrasement ne s'est pas fait."
                    ;;
            esac
        fi
    fi
else
    echo "Absence du fichier SEC."
fi
