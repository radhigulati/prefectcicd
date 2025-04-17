from prefect import flow, task
import pandas as pd
from datetime import datetime
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

@task
def create_data():
    """Create a simple DataFrame"""
    data = {
        'timestamp': [datetime.now()],
        'message': ['Hello from Prefect!']
    }
    return pd.DataFrame(data)

@task
def save_data(df):
    """Save the DataFrame to a CSV file"""
    df.to_csv('output.csv', index=False)
    return "Data saved successfully!"

@flow(name="Simple Prefect Flow")
def main_flow():
    """Main flow that orchestrates the tasks"""
    df = create_data()
    result = save_data(df)
    print(result)

if __name__ == "__main__":
    # Create a deployment
    deployment = Deployment.build_from_flow(
        flow=main_flow,
        name="scheduled-flow",
        work_pool_name="my-managed-pool",
        schedule=CronSchedule(cron="0 15 * * *"),  # 3:00 PM daily
        infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}}
    )
    deployment.apply() 