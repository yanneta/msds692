## Preprocessing data
As a data scientist, part of your time will be spent processing and reshaping data. In this assignment, you will work on a dataset from a real project I worked on a few years ago. This dataset presents interesting challenges. We will process the data so that it can be used by a time series neural network model.


### Task 1: Processing time periods
Each patient records in the dataset was divided into successive periods. The column 'key' is the identifier for each period. Each period represents 40 lines in the dataset. Here is how we can look at the period with key = '10013_18'.

```
df = pd.read_csv("~/data/icu_data_10013.csv")
df0 = df[df["key"] == "10013_18"]
df0.shape # (40, 28) 
```

The first task is to aggregate the 40 lines into one line. The DataFrame contains some static columns,
whose values do not change within a given period, and time series columns, whose values are variable.
Given a DataFrame for a period, along with a list of static column names `static_cols` and a list of time series columns `time_cols`, the function `process_time_period` will compute a dictionary. The keys in the dictionary will be the column names.
For time series columns, the values will be a list of 40 numbers. For static columns,
the values will be a single number. Before returning, convert the dictionary into a pandas Series.


```def process_time_period(df, static_cols, time_cols):```

### Task 2: Processing all time periods with GroupBy.

Your task is to write a function named `process_all_periods` that processes a DataFrame by aggregating data for each unique key. The function should group the DataFrame by a specified column and apply a provided function to each group. It will aggregate the rows based on the provided static and time series columns. The final output should be a new DataFrame containing the aggregated data for each unique key.

```def process_all_periods(df, static_cols, time_cols, process_time_period, col="key"):```

### Task 3: Split dataset

Your task is to write a function named `split_dataframe_by_column_values` that splits the input DataFrame into training, validation, and test DataFrames based on the specified column values.

```
def split_dataframe_by_column_values(
        df, col, train_values, valid_values, test_values):
```

Also, write a function `split_list_into_three_groups` that, given a list of unique values and three probabilities, splits the list into three groups based on the specified probabilities.

```
def split_list_into_three_groups(values, p1, p2, p3):
``` 

### Task 4: Encode categorical variables and normalize
In this task, you will implement two functions: `encode_category` and `normalize_var`. These functions will be used to process data in a pandas DataFrame.


Label encoding is a technique used to convert categorical variables into a numerical format that can be used in machine learning models. It assigns a unique integer to each distinct category or label in the categorical variable. Write a function called label_encoding that, given a DataFrame, a column, and a mapping from categories to integers, will apply label encoding to that column.

```
def encode_category(df, col, cat_map):
```

You will implement the `compute_category_map` function, which computes a mapping from unique categorical values to integers. This is useful for encoding categorical data in a format suitable for machine learning models.

```
def compute_category_map(values):
```

You need to implement the normalize_var function, which normalizes a column in a DataFrame using the provided mean and standard deviation.

```
def normalize_var(df, col, mean, std):
```


### Task 5: Put it all together.



## Deliverables:

1. Complete all functions in `processing.py.`
2. Pass the pytest tests.
3. Complete Task 5 in `processing_dataset.ipynb`.
4. Push `processing.py` and `processing_dataset.ipynb` to Github.

