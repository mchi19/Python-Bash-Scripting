#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-09-03 13:13:36 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
if [[ $# != 1 ]]
then 
    echo -e "Usage: sort_logs.bash <input file>\n"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo -e "Error: $1 is not a readable file.\n"
    exit 2
fi

###removing files###
if [[ -e ${1}.unsorted ]]
then
    rem1=$(rm -f ${1}.unsorted)
    if (( $rem1 ))
    then
        echo "Error: Could not remove ${1}.unsorted"
        exit 3
    else
        echo "Note: Removing existing file ${1}.unsorted"
    fi
fi
if [[ -e ${1}.sorted ]]
then
    rem2=$(rm -f ${1}.sorted)
    if (( $rem2 ))
    then
        echo "Error: Could not remove ${1}.sorted"
        exit 3
    else
        echo "Note: Removing existing file ${1}.sorted"
    fi
    echo
    exit 0
fi

###unsorted###
exec 3>${1}.unsorted
exec 4<$1
flag=1
init=1
while read -a data <&4
do
    len=${#data[*]}
    ((mlen=$len-1))
    if [[ $flag == 1 ]]
    then
        if [[ $init == 1 ]]
        then
            tarr=(${data[1]})
            init=0
        fi
        for ((x=2; x<len; x++))
        do
            tarr+=" ${data[x]}"
            mnarr=($tarr)
        done
        flag=0
    else
        for ((i=1; i<len; i++))
        do
            time=${data[0]}
            name=${mnarr[$i-1]}
            tempt=${data[i]} 
            echo "$name,$time,$tempt" >&3
        done    
    fi    
done
echo >&3

###sorted###
exec 5<${1}.unsorted
exec 6>${1}.sorted
temp=$(while read data <&5; do echo ${data}; done | sort -n -t ',' -k 3r -k 1)
echo "${temp[*]}" >&6
echo >&6

###output###
exec 8<$1
exec 7>${1}.out
flag=1

while read -a data <&8
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
        echo "Average temperature for time $time was $avg_temp C." >&7
        temp=($(for ((i=1; i<len; i++)); do echo ${data[$i]}; done | sort -n))
        if (( $len1%2 == 0 ))
        then
            ((ind=(len1/2)-1))
            ((ind1=$ind+1))
            t1=${temp[ind]}
            t2=${temp[ind1]}
            med=$(echo 'scale=2;'"(($t1+$t2)/2)"|bc -l)
        else
            ((ind=($len1+1)/2))
            med="${temp[$ind-1]}.00"
        fi
        echo -e "Median temperature for time $time was $med C.\n" >&7
    fi
    flag=0
done
flag=1
for ((i=1; i<len; i++))
do
    tarr=($(while read line; do tline=($line); echo ${tline[i]}; done <$1 | sort -n))
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
    fi
    echo "Average temperature for ${tarr[0]} was $avg C." >&7
    echo -e "Median temperature for ${tarr[0]} was $tmed C.\n" >&7
done
echo
exit 0

