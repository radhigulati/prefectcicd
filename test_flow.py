import pytest
from prefect import flow
from flow import main_flow, create_data, save_data
import pandas as pd
from datetime import datetime
import os

def test_create_data():
    """Test that create_data task returns a DataFrame with correct columns"""
    result = create_data()
    assert isinstance(result, pd.DataFrame)
    assert 'timestamp' in result.columns
    assert 'message' in result.columns
    assert len(result) == 1

def test_save_data():
    """Test that save_data task saves the DataFrame correctly"""
    # Create test data
    test_df = pd.DataFrame({
        'timestamp': [datetime.now()],
        'message': ['Test message']
    })
    
    # Run the task
    result = save_data(test_df)
    
    # Verify the result
    assert result == "Data saved successfully!"
    assert os.path.exists('output.csv')
    
    # Clean up
    if os.path.exists('output.csv'):
        os.remove('output.csv')

def test_main_flow():
    """Test the entire flow"""
    # Run the flow
    result = main_flow()
    
    # Verify the flow completed successfully
    assert result is None  # Since our flow just prints
    
    # Clean up
    if os.path.exists('output.csv'):
        os.remove('output.csv') 