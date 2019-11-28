import serial
import psycopg2
from time import sleep
from datetime import datetime
from random import randint

# Make connection with the database
def db_connect():
	con = psycopg2.connect("dbname=datacentersupervisor user=postgres host=localhost password=postgres")
	cursor = con.cursor()
	return con, cursor

def insert_from_serial(temperature, humidity, gas, date):
	con, cursor = db_connect()
	cursor.execute(f"INSERT INTO main_collection (temperature, humidity, gas, date) VALUES ({temperature}, {humidity}, {gas}, '{date}');")
	con.commit()
	con.close()
	print('Insert accomplished!')

#---------------------------------------------------------------------
# Starting server
#---------------------------------------------------------------------

print('Server started...')

# Serial code
se = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:
	# Reading serial
	try:
		data = se.readline()
		if data:
			data_clear = data.decode().split("|")
			date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			insert_from_serial(data_clear[0], data_clear[1], data_clear[2], date)
	except Exception as err:
		print(f"Ocorreu um problema: {err}")
