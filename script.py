import pandas as pd
from datetime import datetime, timedelta
import time

# Read the CSV file into a DataFrame
df = pd.read_csv('dummy_data_CB.csv')

# Main script
while True:
    # Specify the columns from which you want to extract random data
    columns_to_extract = ['Code Cost Bucket', ' Description', 'Code Sub CB', 'Code and Description', 'Amount']

    # Set the number of random rows to extract
    num_rows_to_extract = 2

    # Get the last date in the existing data
    last_date = pd.to_datetime(df['Date'].iloc[-1], format='%Y-%m-%d')

    # Generate new rows with increasing dates
    new_dates = [last_date + timedelta(days=i) for i in range(1, num_rows_to_extract + 1)]

    # Randomly choose multiple row indices
    random_row_indices = df.sample(n=num_rows_to_extract).index

    # Extract random rows from the specified columns based on the chosen row indices
    random_data = df.loc[random_row_indices, columns_to_extract].copy()

    # Remove the hours, minutes, and seconds from the new dates
    new_dates = [date.strftime('%Y-%m-%d') for date in new_dates]

    # Assign the new dates to the 'Date' column in the random data
    random_data['Date'] = new_dates

    # Append the random data to the existing DataFrame
    df = pd.concat([df, random_data], ignore_index=True)

    # Save the updated DataFrame as an Excel file
    df.to_csv('dummy_data_CB.csv', index=False)

    # Wait for 5 minutes before generating the next data
    time.sleep(300)
