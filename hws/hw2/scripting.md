*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*


## Goal
The assignment aims to enhance practical skills in shell scripting and command-line data processing, which are valuable for automation. 


### Task 1:

Given a log file (example: data_domset_4-12-0.2_d_0.9_e60_p_c.log), create a shell script that collects the training statistics. The training statistics are located on the lines that start with “INFO:root:Train”. The output format should be a CSV printed to the standard output with the header: “epoch,med_flips,mean_flips,med_backflips,mean_backflips,accuracy,loss. Each line of the output corresponds to the result of one epoch of training. Here is an example:

This line 
INFO:root:Train Ep 51 Flips Med: 63.00, Mean: 89.43 Backflips Med: 23.00 Mean: 48.64 Acc: 100.00 Loss: 0.42

Results in this output:
51,63.00,89.43,23.00, 48.64,100.00,0.42

**Deliverables:**
A script named `stats_per_experiment.sh` that takes as an argument the path to a specific log file.
`./test_stats_per_experiment.sh ~/data/train_logs/data_domset_4-12-0.2_d_0.3_e60.log `

Return a to standard output content that starts with:
epoch,med_flips,mean_flips,med_backflips,mean_backflips,accuracy,loss
1,211.00,426.91,173.00,386.28,99.95,0.03
2,183.00,352.15,142.00,311.54,100.00,0.03
3,156.00,299.42,116.00,258.95,100.00,0.03
4,127.00,248.45,87.00,208.04,100.00,0.03
5,102.00,183.38,63.00,143.12,100.00,0.03


Testing:
 Run test_stats_per_experiment.sh with a path to the logs
`./test_stats_per_experiment.sh ~/data/train_logs` 
The files are identical.


### Task 2:
Given a log file (example: data_domset_4-12-0.2_d_0.9_e60_p_c.log), create a script that collects the evaluation statistics. The information on evaluation is found on 4 consecutive lines. Here is an example:

INFO:root:EVAL  Ep 55 Flips Med: 62.50, Mean: 92.39 Backflips Med: 22.00 Mean: 51.70 Acc: 100.00 Loss: 0.43
INFO:root:CI means FLIPS (90.41, 98.13), CI median (62.00, 62.00)
INFO:root:CI means BACKFLIPS (49.89, 57.69), CI median (22.00, 22.00)
INFO:root:parms [0.13 0.36] 0.01


The output format should be a CSV printed to the standard output with the header:
“Epoch,med_flips,mean_flips,accuracy,loss,ci_mean_flips1,ci_mean_flip_2,ci_med_flips1,ci_med_flip_2,parm1,parm2,parm3”

Example output:
55,62.50,92.39,100.00,0.43,90.41, 98.13,62.00,62.00,0.13,0.36,0.01
 
Note that the eval lines that we are interested in start at epoch 5( `Ep 5`.) 

Deliverables:
A script named `stats_per_experiment_eval.sh`

Testing:
 Run test_stats_per_experiment.sh with a path to the logs
 `./test_stats_per_experiment_eval.sh ~/data/train_logs`
The files are identical.



### Task 3:
In this task we will summarize all experiments. Each logs file has a line like:

INFO:root:Best Flips Med: 49.75, Best epoch: 25

Where the best median flips and the best epochs are summarized. That line is from data_domset_4-12-0.2_d_0.3_e60_p_c.log 

We would like to create a csv content in which the header is:

“dataset,size,d,num_epochs,best_med_flips,best_epoch”

The information for the first 4 columns comes from the filename itself. The last two columns come from the line that starts with “INFO:root:Best Flips Med”.

For the data_domset_4-12-0.2_d_0.3_e60_p_c.log this would look like:

domset,4-12-0.2,0.3,60, 49.75,25


Deliverables:
A script named `best_flips_all_experiments.sh`

Testing:
 Run test_best_flips_all_experiments.sh with a path to the logs

`./test_best_flips_all_experiments.sh  ~/data/train_logs`
The files are identical.


