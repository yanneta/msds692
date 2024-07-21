#!/bin/sh


path_to_logs=$1

./best_flips_all_experiments.sh $path_to_logs > temp3.csv

if diff temp3.csv sample_output3.csv > /dev/null; then
    echo "The files are identical."
else
    echo "The files are different."
fi

rm temp3.csv
