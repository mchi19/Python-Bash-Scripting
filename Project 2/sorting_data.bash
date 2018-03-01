#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-09-05 15:31:20 -0400 (Tue, 05 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
if [[ $# != 1 ]]
then
    echo -e "Usage: ./sorting_data.bash <inpute file>\n"
    exit 1
fi


if [[ ! -r $1 ]]
then
    echo -e "Error: $1 is not a readable file.\n"
    exit 2
fi

echo "Your choices are: "
echo "1) First 10 people"
echo "2) Last 5 names by highest zipcode"
echo "3) Address of 6th-10th by reverse e-mail"
echo "4) First 12 companies"
echo "5) Pick a number of people"
echo "6) Exit"

while (( 1 ))
do
    echo -n "Your choice: "
    read usr_c
    if [[ $usr_c == 1 ]]
    then
        tail -n +2 $1 | sort -t "," -k 7,7 -k 5,5 -k 2,2 -k 1,1| head -n 10
    elif [[ $usr_c == 2 ]]
    then
        tail -n +2 $1 | sort -n -t "," -k 8,8 | tail -n 5 | cut -d ',' -f 1-2
    elif [[ $usr_c == 3 ]]
    then
        tail -n +2 $1 | sort -r -t "," -k 11,11 | head -n 10 | tail -n 5 | cut -d ',' -f 4
    elif [[ $usr_c == 4 ]]
    then
        tail -n +2 $1 | sort -t "," -k 3,3 | cut -d "," -f 3 | head -n 12 
    
    elif [[ $usr_c == 5 ]]
    then
        echo -n "Enter a number: "
        read num
        tail -n +2 $1 | sort -t "," -k 2,2 -k 1,1 | head -n $num
    
    elif [[ $usr_c == 6 ]]
    then
        echo "Have a nice day!"
        echo
        exit 0
    else
        echo "Error! Invalid Selection!"
    fi

done
