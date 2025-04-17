# Prefect GitHub Actions Demo

This is a simple demonstration of using Prefect with GitHub Actions for workflow automation.

## Project Structure

- `flow.py`: Contains a simple Prefect flow that creates and saves data
- `requirements.txt`: Lists the Python dependencies
- `.github/workflows/prefect_flow.yml`: GitHub Actions workflow configuration
- `test_flow.py`: Test file for the Prefect flow

## Setup

1. Add GitHub Secrets:
   - Go to Repository Settings → Secrets and variables → Actions
   - Add these secrets:
     - `PREFECT_API_KEY`: Your Prefect Cloud API key
     - `PREFECT_WORKSPACE`: Your Prefect Cloud workspace ID

2. The workflow will:
   - Run tests on every push to main
   - If tests pass, deploy to Prefect Cloud
   - The flow will run daily at 3:00 PM

## How It Works

1. The Prefect flow (`flow.py`) contains two tasks:
   - `create_data()`: Creates a simple DataFrame with a timestamp and message
   - `save_data()`: Saves the DataFrame to a CSV file

2. The GitHub Actions workflow:
   - Triggers on pushes to the main branch or manual workflow dispatch
   - Sets up Python 3.9
   - Installs dependencies
   - Runs tests
   - If tests pass, deploys to Prefect Cloud

## Running the Flow

The flow will automatically run when you push to the main branch. You can also manually trigger it using the GitHub Actions interface.

## Requirements

- Python 3.9+
- Prefect 2.0+
- pandas 1.3+
- pytest 7.0+ 