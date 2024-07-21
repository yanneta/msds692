#!/bin/sh


path_to_logs=$1

./stats_per_experiment_eval.sh $path_to_logs/data_domset_4-12-0.2_d_0.3_e60_p_c.log > temp2.csv

if diff temp2.csv sample_output2.csv > /dev/null; then
    echo "The files are identical."
else
    echo "The files are different."
fi

rm temp2.csv
