import sys
import os
"""
Lab 2 — Learner Test File

Write your own pytest tests here. You must implement at least 3 test functions:
  - test_load_data_returns_dataframe
  - test_clean_data_no_nulls
  - test_add_features_creates_revenue

The autograder will run your tests as part of the CI check.
"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import numpy as np
import pytest
from pipeline import load_data, clean_data, add_features

DATA_PATH_FOR_TEST = 'data/sales_records.csv'

# ─── Test 1 ───────────────────────────────────────────────────────────────────

def test_load_data_returns_dataframe():
    """load_data should return a DataFrame with expected columns and rows."""
    # TODO: Call load_data('data/sales_records.csv')
    df = load_data(DATA_PATH_FOR_TEST)

    # TODO: Assert the result is a pd.DataFrame
    assert isinstance(df, pd.DataFrame)

    # TODO: Assert len(df) > 0
    assert len(df)>0
    # TODO: Assert all expected columns are present:
    #        'date', 'store_id', 'product_category', 'quantity', 'unit_price', 'payment_method'
    expected_columns = ['date', 'store_id', 'product_category', 'quantity', 'unit_price', 'payment_method']

# ─── Test 2 ───────────────────────────────────────────────────────────────────

def test_clean_data_no_nulls():
    """After clean_data, quantity and unit_price should have no NaN values."""
    # TODO: Load the data, then call clean_data
    raw_df = load_data(DATA_PATH_FOR_TEST)
    cleaned_df = clean_data(raw_df)

    # TODO: Assert cleaned['quantity'].isna().sum() == 0
    assert cleaned_df['quantity'].isna().sum() == 0

    # TODO: Assert cleaned['unit_price'].isna().sum() == 0
    assert cleaned_df['unit_price'].isna().sum() == 0



# ─── Test 3 ───────────────────────────────────────────────────────────────────

def test_add_features_creates_revenue():
    """add_features should add a 'revenue' column equal to quantity * unit_price."""
    # TODO: Load and clean the data, then call add_features
    raw_df = load_data(DATA_PATH_FOR_TEST)
    cleaned_df = clean_data(raw_df)
    enriched_df = add_features(cleaned_df)   
    # TODO: Assert 'revenue' in df.columns
    assert 'revenue' in enriched_df.columns
    expected_revenue = enriched_df['quantity'] * enriched_df['unit_price']

    # TODO: Assert the revenue values equal quantity * unit_price
    #        Use pd.testing.assert_series_equal for float comparison
    pd.testing.assert_series_equal(enriched_df['revenue'], expected_revenue,check_names=False)
