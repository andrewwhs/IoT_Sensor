FROM python:3
RUN apt update \
 && apt install unixodbc -y \
 && apt install freetds-dev -y \
 && apt install freetds-bin -y \
 && apt install tdsodbc -y \
 && apt install --reinstall build-essential -y

# populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so"

#Working directory
WORKDIR /app
#Install python package
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy all files from this directory
COPY ./* .
#run python 
CMD [ "python", "./Createtable.py" ]
CMD [ "python", "./IoTSensor.py" ]