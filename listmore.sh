#!/bin/bash 

CNUM=${1-1280}

echo "== less than $CNUM (char), but has more tag"
echo "========================================"
find . -size -${CNUM}c -name "*markdown" -exec grep -l "<\!-- more" {} \;
echo "== more than $CNUM (char), but has no more tag"
echo "========================================"
find . -size +${CNUM}c -name "*markdown" -exec grep -L "<\!-- more" {} \;
