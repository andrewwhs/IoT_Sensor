#connect to SQL server
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-5H91B2GU\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
#Create SQL Table 
cursor.execute('''
    IF OBJECT_ID('dbo.IoTSensor_reading', 'U') IS NOT NULL
    DROP TABLE dbo.IoTSensor_reading
    CREATE TABLE dbo.IoTSensor_reading
    (
        id INT IDENTITY(1,1) PRIMARY KEY,  -- primary key column
        timestamp [VARCHAR](50) NOT NULL,
        sensorName [VARCHAR](50) NOT NULL,
        value [VARCHAR] (50) NOT NULL
        -- specify more columns here
        index time_index(timestamp, sensorName)
    );
    ''')
conn.commit()          