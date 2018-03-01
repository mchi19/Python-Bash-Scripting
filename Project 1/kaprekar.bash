#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-08-29 17:03:25 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
if [[ $# != 1 ]]
then
    echo -e "Usage: kaprekar.bash <non-negative integer>\n"
    exit 1
fi

if (( $1 <= 0 ))
then
    echo -e "Error: please enter a non-negative integer.\n"
    exit 2
fi
num=$1
x=1

while (( x <= num ))
do
    ((square=x*x))
    xd=${#x} #n digit of in original number
    sd=${#square} #n digits in squared 
    ((txd=$sd-$xd+1)) 
    if [[ $sd == 1 ]]
    then
        rn=$(echo "$square" | cut -c $xd-$sd)
    else
        rn=$(echo "$square" | cut -c $txd-$sd)  
    fi
    
    if [[ $sd == 1 ]] 
    then
        ln=0
    elif (( $xd*2 > $sd ))
    then
        ((xdd=$xd-1))
        ln=$(echo "$square" | cut -c 1-$xdd)
    else
        ln=$(echo "$square" | cut -c 1-$xd)
    fi
    trn=$((10#$rn))
    tln=$((10#$ln))
    ((kap=$trn+$tln))
    #echo $kap
    tkap=$((10#$kap))
    if [[ $x == $tkap ]]
    then
        echo "$x, square=$square, $rn+$ln=$tkap"
    fi
    ((x=x+1))
done


exit 0
