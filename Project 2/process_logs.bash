#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-09-03 13:13:21 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
if [[ $# != 1 ]]
then
    echo -e "Usage: process_logs.bash <input file>\n"
    exit 1
fi
file=$1
if [[ ! -r $file ]]
then
    echo -e "Error: $file is not a readable file.\n"
    exit 2
fi
flag=1
exec 3>${file}.out
exec 4<$file

while read -a data <&4
do
    len=${#data[*]}
    ((len1=$len-1))
    sum=0
    time=${data[0]}
    if [[ $flag == 0 ]]
    then
        for ((x=1; x<len; x++))
        do
            ((sum=${data[x]}+sum))
        done
        avg_temp=$(echo 'scale=2;'"$sum/$len1"|bc -l)
        echo "Average temperature for time $time was $avg_temp C." >&3
        temp=($(for ((i=1; i<len; i++)); do echo ${data[$i]}; done | sort -n))
        if (( $len1%2 == 0 ))
        then
            ((ind=(len1/2)-1))
            ((ind1=$ind+1))
            t1=${temp[ind]}
            t2=${temp[ind1]}
            med=$(echo 'scale=2;'"(($t1+$t2)/2)"|bc -l)
            #med=$(echo 'scale=2;'"((${temp[ind]}+${temp[ind1]})/2)"|bc -l)
        else
            ((ind=($len1+1)/2))
            med="${temp[$ind-1]}.00"
            #med=${temp[ind]}
            #med=$(echo 'scale=2;'"(${temp[ind]}/1.0)"|bc -l)
        fi
        echo -e "Median temperature for time $time was $med C.\n" >&3
    fi
    flag=0
done
flag=1
for ((i=1; i<len; i++))
do
    tarr=($(while read line; do tline=($line); echo ${tline[i]}; done <$file | sort -n))
    tlen=${#tarr[*]}
    ((tlen1=$tlen-1))
    sum=0
    for ((j=1; j<tlen; j++))
    do
        ((sum=sum+${tarr[j]}))       
    done
    avg=$(echo 'scale=2;'"$sum/$tlen1"|bc -l)
    if (( $tlen1%2 == 0 ))
    then
        ((tind=(tlen1/2)-1))
        ((tind1=$tind+1))
        tt1=${temp[tind]}
        tt2=${temp[tind1]}
        tmed=$(echo 'scale=2;'"((${tarr[tind]}+${tarr[tind1]})/2)"|bc -l)
    else
        ((tind=($tlen1+1)/2))
        #lol? fix this shit below
        tmed="${tarr[tind]}.00"
        #tmed=$(echo 'scale=2;'"(${temp[tind]}/1.0)"|bc -l)
    fi
    echo "Average temperature for ${tarr[0]} was $avg C." >&3
    echo -e "Median temperature for ${tarr[0]} was $tmed C.\n" >&3
done
echo
exit 0
