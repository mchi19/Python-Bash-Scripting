#! /bin/bash

# $Author: ee364c12 $
# $Date: 2017-09-05 17:04:27 -0400 (Tue, 05 Sep 2017) $

function array 
{
    # Fill out your answer here.
    ((x=$RANDOM%5))
    Arr=(a.txt b.txt c.txt d.txt e.txt)    
    file=${Arr[x]}
    head -n 9 $file | tail -n 3

    return 
    

}


#
# To test your function, you can call it below like this:
#
array
#
