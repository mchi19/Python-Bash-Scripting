#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-08-24 14:01:28 -0400 (Thu, 24 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
while ((1))
do
    echo -n "Enter a command: "
    read response
    if [[ $response == hello ]]
    then
        echo -e "Hello $USER \n"
    elif [[ $response == quit ]]
    then
        echo "Goodbye"
        exit 0
    elif [[ $response == compile ]]
    then
        for File in *.c
        do
            name=$(echo $File | cut -f 1 -d '.')
            gcc -Wall -Werror $File -o $name.o
            if [[ $? == 1 ]]
            then
                echo "Compilation failed for: $File"
            else
                echo "Compilation succeeded for: $File"
            fi
        done
        echo 
    elif [[ $response == whereami ]]
    then
        echo -e $PWD "\n"
    else
        echo -e "Error: unrecognized input\n"
    fi
done

