#!/bin/bash

MSG="This will run the TSP_WesternSahara_29.txt data set"

echo "Running 20 times..."

for i in {1..20}
do
	echo ""
    echo "" >> "WesternSahara.txt"
    echo "Run " $i >> "WesternSahara.txt"
    python3 main.py >> "WesternSahara.txt"
	echo "Run " $i " done"
done


echo "done"
