#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-08-29 17:19:12 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if [[ $# != 1 ]]
then
    echo -e "Usage: check_permissions.bash <input file/directory>\n"
    exit 1
fi

perm=$(ls -ld $@)
echo $perm

len=${#perm}
x=1
while (( $x<$perm  ))
do
    if (( x == 1 ))
    then
        p1=$(echo "$perm" | cut -c $x)
        if [[ $p1 == "-" ]]
        then
            echo -e "$1 is an ordinary file\n"
        elif [[ $p1 == "d" ]] 
        then
            echo -e "$1 is a directory\n"
        fi
    fi

    ((x=x+1))
done


