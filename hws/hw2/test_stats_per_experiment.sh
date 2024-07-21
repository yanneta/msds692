#!/bin/sh


path_to_logs=$1

./stats_per_experiment.sh $path_to_logs/data_domset_4-12-0.2_d_0.3_e60_p_c.log > temp.csv

if diff temp.csv sample_output1.csv > /dev/null; then
    echo "The files are identical."
else
    echo "The files are different."
fi

rm temp.csv
