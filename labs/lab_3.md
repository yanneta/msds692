# Data Processing and Text Manipulation Exercises

### Exercise 1: Filter and Extract Data from a Log File

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

### Exercise 2: Book List Manipulation

Create a file with the following content:
```plaintext
1. The Great Gatsby; F. Scott Fitzgerald; 1925; Fiction
2. To Kill a Mockingbird; Harper Lee; 1960; Fiction
3. 1984; George Orwell; 1949; Dystopian
4. Pride and Prejudice; Jane Austen; 1813; Romance
5. The Catcher in the Rye; J.D. Salinger; 1951; Fiction
6. Brave New World; Aldous Huxley; 1932; Dystopian
7. The Hobbit; J.R.R. Tolkien; 1937; Fantasy
8. The Lord of the Rings; J.R.R. Tolkien; 1954; Fantasy
9. The Diary of a Young Girl; Anne Frank; 1947; Biography
10. The Picture of Dorian Gray; Oscar Wilde; 1890; Fiction
```
Tasks:
1. Find all lines in books.txt that start with either the number 1 or 2.
2. Extract and filter authors starting with J or F.
3. Find lines that contain the year '19' followed by any digit.
4. Exclude all lines that end in 'Fiction'.
5. Extract lines that end in 'Fiction' or 'Fantasy'.

