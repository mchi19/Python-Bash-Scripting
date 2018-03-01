#! /bin/bash

#----------------------------------
# $Author: ee364c12 $
# $Date: 2017-09-26 17:20:29 -0400 (Tue, 26 Sep 2017) $
#----------------------------------

function part_a 
{               
    ((x=$RANDOM%4))
    Arr=(a.txt b.txt c.txt d.txt)
    file=${Arr[x]}
    head -n 6 $file | tail -n 3
    return                      
}                               

function part_b
{              
    name=$1
    if [[ -e $name ]]
    then
        echo -e "$name is a file name.\n"
    elif [[ -d $name ]] 
    then
        echo -e "$name is a directory name.\n"
    else
        echo -e "$name is not a file or directory name.\n"
    fi
    return                     
}                              

function part_c
{
    #exec 3>$file.txt
    file=$1
    #file="file.txt"
    #if  
    return
}

function part_d
{
    x=$(wc -w temp.txt)
    y=$(wc -l temp.txt)

    echo "temp.txt has $x words and $y lines."   
    return
}

function part_e
{
    python3.4 ece364.py >> output.txt 2>&1 
    return
}

function part_f
{
    file=people.csv
    tail -n +2 $file | sort -t "," -k 4,4 -k 6,6 -k 1,1 -k 2,2 | tail -n 10
    return
}

function part_g
{
    #input="multimillionaire"
    val="m u l t i m i l l i o n a i r e"
    arr=($val)
    #vows="a e i o u"
    #va=($vows)
    res=()
    for i in ${arr[*]}
    do
        if [[ $i == 'a' ]] || [[ $i == 'e' ]] || [[ $i == 'i' ]] || [[ $i == 'o' ]] || [[ $i == 'u' ]]
        then
            i="-"
        fi
    done
    echo ${arr[*]} 
    return
}


function part_h
{
    files=(./src/*.c)
    for i in ${files[*]}
        if gcc i 1>/dev/null
        then
            echo "$i: success"
        else
            echo "$i: failure"
        fi 
    return
}

function part_i
{
    # Fill out your answer here
    return
}

function part_j
{
    # Fill out your answer here
    return
}

# To test your function, you can call it below like this:
#
# part_a
part_h
