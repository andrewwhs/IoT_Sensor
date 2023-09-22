#connect to SQL server
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-5H91B2GU\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
   
#Import CSV file
import pandas as pd
import glob
# Get a list of all CSV files in a directory
csv_files = glob.glob('./csvfiles/*.csv')
# Create an empty dataframe to store the combined data
combined_df = pd.DataFrame()
# Loop through each CSV file and append its contents to the combined dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    #Removes non-numeric value
    df['value'] = pd.to_numeric(df['value'], errors = 'coerce')
    print(df)
    df = df.dropna()
    print(df)
    #timestamp to ISO8601 format
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(df)
    combined_df = pd.concat([combined_df, df])

# Print the combined dataframe
print(combined_df)

#Insert data
for row in combined_df.itertuples():
    cursor.execute('''
                INSERT INTO IoTSensor_reading (timestamp, sensorName, value)
                VALUES (?,?,?)
                ''',
                row.timestamp, 
                row.sensorName,
                row.value
                )
conn.commit()

#Delete duplicate data (same timestamp, sensorName, value)
cursor.execute('''
    delete from master.dbo.IoTSensor_reading
    where id not in
    (
        select min(id)
        from master.dbo.IoTSensor_reading
        group by timestamp, sensorName, value
    );
    ''')
conn.commit()          