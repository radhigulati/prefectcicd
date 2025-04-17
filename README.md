# Prefect GitHub Actions Demo

This is a simple demonstration of using Prefect with GitHub Actions for workflow automation.

## Project Structure

- `flow.py`: Contains a simple Prefect flow that creates and saves data
- `requirements.txt`: Lists the Python dependencies
- `.github/workflows/prefect_flow.yml`: GitHub Actions workflow configuration

## How It Works

1. The Prefect flow (`flow.py`) contains two tasks:
   - `create_data()`: Creates a simple DataFrame with a timestamp and message
   - `save_data()`: Saves the DataFrame to a CSV file

2. The GitHub Actions workflow:
   - Triggers on pushes to the main branch or manual workflow dispatch
   - Sets up Python 3.9
   - Installs dependencies
   - Runs the Prefect flow

## Running the Flow

The flow will automatically run when you push to the main branch. You can also manually trigger it using the GitHub Actions interface.

## Requirements

- Python 3.9+
- Prefect 2.0+
- pandas 1.3+ 