#! /bin/bash

#---------------------------------------
# $Author: ee364c12 $
# $Date: 2017-09-03 13:13:48 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.
cd c-files
for file in *.c
do
    fn=$(echo $file | cut -f 1 -d '.')
    echo -n "Compiling file $file... "
    if ! (gcc -Wall -Werror $file 2>/dev/null)
    then
        echo "Error: Compilation failed."
    else
        exec 3>${fn}.out
        echo "Compilation succeeded."
        a.out >&3
    fi
done
echo
exit 0
