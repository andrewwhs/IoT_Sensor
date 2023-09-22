# IoTSensor

This repository is about creating a table in SQL server, then importing csv files with timestamp, sensor name, and sensor value in it. Non-valid records will be eliminated.


## Usage
1. Create a SQL server https://www.microsoft.com/en-us/sql-server/sql-server-downloads (Express)
2. In Createtable.py and IoTSensor.py, search for "LAPTOP-5H91B2GU\SQLEXPRESS" and change it to your own server name.
3. Install the packages need in requirements.txt
4. ./csvfiles contains the data for testing
5. Run Createtable.py
6. Run IoTSensor.py


## Test cases
Test cases are provided in Test_cases.txt

## More to be done
Dockerfile


## Authors
[@andrewwhs](https://github.com/andrewwhs)