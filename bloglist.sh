#!/bin/bash 

for file in *; do
    if [ -d $file ];then
        echo $file `grep '<article>' $file/index.html | wc -l`
    fi
done
