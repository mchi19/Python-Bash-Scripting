#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-08-24 14:01:46 -0400 (Thu, 24 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
if [[ $# != 2 ]]
then
    echo -e "Usage: ./game_stats.bash <file> <game>\n"
    exit 1 
fi
file=$1
game=$2
if [[ ! -e $file ]]
then
    echo -e "Error: $file does not exist\n"
    exit 2
fi
if [[ $game ]]
then
    tot_st=0
    tot_hr=0
    top_t=0
    bot_t=1
    while read line
    do
        name=$(echo "$line" | cut -d "," -f 1)
        tgame=$(echo "$line" | cut -d "," -f 2)
        thr=$(echo "$line" | cut -d "," -f 3)
        #echo $name $tgame $thr
        if [[ $tgame == $game ]]
        then
            ((tot_st=tot_st+1))
            ((tot_hr=tot_hr+thr))
            if (( $thr >= $top_t ))
            then
                top_n=$name
                top_t=$thr
            fi
            if (( $thr <= $bot_t ))
            then
                bot_n=$name
                bot_t=$thr
            fi
        fi
        #echo $line
    done <$file
    echo "Total students: $tot_st"
    echo "Total hours spent in a day: $tot_hr"
    echo "$top_n spent the highest amount of time in a day: $top_t"
    echo -e "$bot_n spent the least amount of time in a day: $bot_t\n" 
    exit 0
fi






