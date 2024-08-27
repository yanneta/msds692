# Data Processing and Text Manipulation Exercises

## Exercise 1: Filter and Extract Data from a Log File

### Given Data

Download and use the following data:

```plaintext
2024-01-01 09:00:00,12345,Deposit,1000.00,Success
2024-01-02 09:05:00,12346,Withdrawal,500.00,Success
2024-01-03 09:10:00,12347,Deposit,700.00,Failure
2024-01-04 09:15:00,12348,Deposit,300.00,Success
2024-01-05 09:20:00,12349,Withdrawal,200.00,Failure
2024-01-06 09:25:00,12350,Deposit,150.00,Success
```
Tasks:
1. Filter the lines that have "Success".
2. Select the appropriate columns to produce a file with the following format:

```plaintext
2024-01-01,Deposit
2024-01-02,Withdrawal
2024-01-04,Deposit
2024-01-06,Deposit
```

