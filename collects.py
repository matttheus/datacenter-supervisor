import serial
import psycopg2
from time import sleep
from datetime import datetime
import threading as th

# Make connection with the database
def db_connect():
	con = psycopg2.connect("dbname=datacentersupervisor user=postgres host=localhost password=postgres")
	cursor = con.cursor()
	return con, cursor

def insert(temperature, humidity, gas, date, time_sleep):
	sleep(time_sleep)
	con, cursor = db_connect()
	
	try:
		cursor.execute(f"INSERT INTO main_collection (temperature, humidity, gas, date) VALUES ({temperature}, {humidity}, {gas}, '{date}');")
	except Exception as err:
		print(f"Ocorreu um problema: {err}")

	con.commit()
	con.close()
	print(f'Insert accomplished! - {th.currentThread().getName()}')

#---------------------------------------------------------------------
# Starting server
#---------------------------------------------------------------------

print('Server started...')

# Serial code
try:
	se = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except Exception as err:
	print(f"Ocorreu um problema: {err}")
	exit(1)

mq2_sleep_time = 15
dht11_sleep_time = 25

while True:
	# Reading serial
	try:
		data = se.readline()
		if data:
			data_clear = data.decode().split("|")
			date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			humidity = data_clear[0] # data_clear
			temperature = data_clear[1] # data_clear
			mq2 = data_clear[2] # data_clear
			dht11_th = th.Thread(target=insert, args=(temperature, humidity, "NULL", date, dht11_sleep_time), name="DHT11")
			dht11_th.start()
			mq2_th = th.Thread(target=insert, args=("NULL", "NULL", mq2, date, mq2_sleep_time), name="MQ2")
			mq2_th.start()
	except Exception as err:
		print(f"Ocorreu um problema: {err}")
