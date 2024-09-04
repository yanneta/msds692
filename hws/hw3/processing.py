import pandas as pd
import numpy as np

def process_time_period(df, static_cols, time_cols):
    """
    Aggregate 40 lines of a DataFrame into one line for a given period.

    This function processes a DataFrame containing both static columns, whose values
    do not change within a given period, and time series columns, whose values are variable.
    It returns a dictionary where the keys are column names. For time series columns,
    the values are lists of 40 numbers, and for static columns, the values are single numbers.
    Before returning, the dictionary is converted into a pandas Series.

    Args:
        df (pd.DataFrame): The DataFrame for a specific period containing 40 rows.
        static_cols (list of str): List of column names that are static 
                                  (values do not change within the period).
        time_cols (list of str): List of column names that are time series 
                                (values vary within the period).

    Returns:
        pd.Series: A Series where the keys are column names, 
                   and the values are lists (numpy arrays) of 40 numbers for time series
                   columns or single numbers for static columns.
    """
    # Your code here


def process_all_periods(df, static_cols, time_cols, process_time_period, col="key"):
    """
    Process all periods in a DataFrame by aggregating data for each unique key.

    This function groups the input DataFrame by the "key" column and applies the
    specified `process_time_period` function to each group. It aggregates the rows
    based on the provided static and time series columns. The result is a new DataFrame
    containing the aggregated data for each unique key.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be processed.
                           It must include a "key" column to group by.
        static_cols (list of str): A list of column names representing static columns,
                                    whose values do not change within the grouped periods.
        time_cols (list of str): A list of column names representing time series columns,
                                  whose values vary within the grouped periods.
        process_time_period (function): A function that processes individual periods
                                         and returns aggregated results for each group.
        col: str: Column used for aggregation.

    Returns:
        pd.DataFrame: A DataFrame containing the aggregated results for each unique key.
                      Each row corresponds to a unique key from the original DataFrame.
    """
    # Your code here


def split_dataframe_by_column_values(
        df, col, train_values, valid_values, test_values):
    """
    Splits the input DataFrame into training, validation, and test
    DataFrames based on the specified column values.

    Args:
        df (pd.DataFrame): The input DataFrame to be split.
        col (str): The name of the column used for splitting.
        train_values (list): The values to include in the training set.
        valid_values (list): The values to include in the validation set.
        test_values (list): The values to include in the test set.

    Returns:
        tuple: A tuple containing three DataFrames:
            - train_df: DataFrame containing training data.
            - valid_df: DataFrame containing validation data.
            - test_df: DataFrame containing test data.
    """
    # Your code here

    return train_df, valid_df, test_df


def split_list_into_three_groups(values, p1, p2, p3):
    """
    Splits a list of unique values into three groups based on specified probabilities.

    Args:
        values (list): A list of unique values to be split.
        p1 (float): The probability for the first group.
        p2 (float): The probability for the second group.
        p3 (float): The probability for the third group.

    Returns:
        tuple: A tuple containing three lists:
            - group1: The first group of values.
            - group2: The second group of values.
            - group3: The third group of values.

    Hint: use np.random.choice
    """
    # Your code here


def encode_category(df, col, cat_map):
    """
    Encode a categorical column in a DataFrame using a provided mapping.

    This function applies label encoding to the specified categorical column in the 
    DataFrame using the provided mapping. If a category is not present in the mapping, 
    it assigns a default value of 0.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        col (str): The name of the categorical column to be encoded.
        cat_map (dict): A dictionary mapping categories to integers.

    Returns:
        pd.DataFrame: A DataFrame with the specified column label encoded.
    """
    # Your code here


def normalize_var(df, col, mean, std):
    """
    Normalize a column in a DataFrame using the provided mean and standard deviation.

    This function standardizes the values in the specified column of the DataFrame
    by subtracting the mean and dividing by the standard deviation. This process
    transforms the data to have a mean of 0 and a standard deviation of 1.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        col (str): The name of the column to be normalized.
        mean (float): The mean value to be used for normalization.
        std (float): The standard deviation value to be used for normalization.

    Returns:
        pd.DataFrame: The DataFrame with the specified column normalized.
    """
    # Your code here


def compute_category_map(values):
    """
    Compute a mapping from unique categorical values to integers.

    This function takes a list of values, extracts the unique values, sorts them,
    and creates a dictionary that maps each unique value to a unique integer starting from 1.

    Args:
        values (list or array-like): A list or array of categorical values.

    Returns:
        dict: A dictionary where the keys are the unique categorical values and the values 
        are unique integers starting from 1.

    Example:
        >>> values = ['apple', 'banana', 'cherry', 'apple']
        >>> compute_category_map(values)
        {'apple': 1, 'banana': 2, 'cherry': 3}
    """
    # Your code here


