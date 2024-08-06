import pandas as pd
import numpy as np
import pytest
from processing import process_time_period, process_all_periods, \
        split_dataframe_by_column_values, split_list_into_three_groups, \
        encode_category, normalize_var, compute_category_map

## put your small data here
df_10013 = pd.read_csv("~/data/icu_data_10013.csv")
df_10013_18 = df_10013[df_10013["key"] == "10013_18"]


def test_process_time_period():
    ser = process_time_period(df_10013_18, ["age", "gender"], ["hr", "spo2"])
    assert ser["age"] == 87
    assert ser["gender"] == 1
    assert list(ser["hr"][:5]) == [110.1, 110.9, 110.3, 109. , 108.1]
    assert ser["hr"].shape[0] == 40
    assert ser["spo2"].shape[0] == 40
    assert ser["spo2"].mean() == pytest.approx(79.1475, rel=1e-9)


def test_process_all_periods():
    result = process_all_periods(df_10013, ["age", "gender"], ["hr", "spo2"], process_time_period)
    assert result.shape == (50, 5)
    assert list(result.columns) == ['key', 'age', 'gender', 'hr', 'spo2']
    assert list(result.key.values[-5:]) == ['10013_68', '10013_69', '10013_70', '10013_71', '10013_72']

def test_split_dataframe_by_column_values():
    # Create a sample DataFrame for testing
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
        'Value': [1, 2, 3, 4, 5, 6, 7]
    }
    df = pd.DataFrame(data)

    # Define the category values for splitting
    train_values = ['A']
    valid_values = ['B']
    test_values = ['C']

    # Call the function to split the DataFrame
    train_df, valid_df, test_df = split_dataframe_by_column_values(
            df, 'Category', train_values, valid_values, test_values)

    # Assertions to check if the output DataFrames are correct
    assert train_df.shape[0] == 3  # There should be 3 rows in the training set (Category 'A')
    assert valid_df.shape[0] == 2   # There should be 2 rows in the validation set (Category 'B')
    assert test_df.shape[0] == 2    # There should be 2 rows in the test set (Category 'C')

    # Check the contents of the DataFrames
    assert list(train_df['Name']) == ['Alice', 'Charlie', 'Grace']
    assert list(valid_df['Name']) == ['Bob', 'Eve']
    assert list(test_df['Name']) == ['David', 'Frank']

    # Check that original DataFrame is unchanged
    assert df.shape[0] == 7  # The original DataFrame should still have 7 rows
    assert list(df['Name']) == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']

    assert list(train_df.index) == list(range(len(train_df)))
    assert list(valid_df.index) == list(range(len(valid_df)))
    assert list(test_df.index) == list(range(len(test_df)))


def test_split_list_into_three_groups():
    # Test with a known set of probabilities
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    p1, p2, p3 = 0.2, 0.5, 0.3

    # Initialize counters for group sizes
    group1_count = 0
    group2_count = 0
    group3_count = 0

    # Run the function multiple times to test probabilistic distribution
    num_iterations = 10000
    for _ in range(num_iterations):
        group1, group2, group3 = split_list_into_three_groups(values, p1, p2, p3)
        group1_count += len(group1)
        group2_count += len(group2)
        group3_count += len(group3)

    # Calculate the observed proportions
    total_count = group1_count + group2_count + group3_count
    observed_p1 = group1_count / total_count
    observed_p2 = group2_count / total_count
    observed_p3 = group3_count / total_count

    # Check if the observed proportions are close to the expected probabilities
    assert abs(observed_p1 - p1) < 0.01, f"Observed p1: {observed_p1}, Expected p1: {p1}"
    assert abs(observed_p2 - p2) < 0.01, f"Observed p2: {observed_p2}, Expected p2: {p2}"
    assert abs(observed_p3 - p3) < 0.01, f"Observed p3: {observed_p3}, Expected p3: {p3}"


def test_encode_category_some_unmapped():
    data = {'category': ['apple', 'banana', 'orange']}
    df = pd.DataFrame(data)
    cat_map = {'apple': 1, 'banana': 2}
    
    result_df = encode_category(df, 'category', cat_map)
    
    expected_data = {'category': [1, 2, 0]}
    expected_df = pd.DataFrame(expected_data)
    
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_normalize_var_basic():
    # Sample DataFrame
    data = {'values': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    # Calculate mean and standard deviation
    mean = df['values'].mean()
    std = df['values'].std()

    # Normalize the column
    result_df = normalize_var(df.copy(), 'values', mean, std)

    # Expected normalized values
    expected_data = {'values': [(x - mean) / std for x in data['values']]}
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)

def test_compute_category_map():
    values = ['cherry', 'banana', 'apple', "banana"]
    expected_output = {'apple': 1, 'banana': 2, 'cherry': 3}
    assert compute_category_map(values) == expected_output

    values = [3, 1, 2, 1]
    expected_output = {1: 1, 2: 2, 3: 3}
    assert compute_category_map(values) == expected_output


