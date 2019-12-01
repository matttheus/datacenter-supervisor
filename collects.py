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

def insert_from_serial(temperature, humidity, gas, date, time_sleep):
	sleep(time_sleep)
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
mq2_sleep_time = 10
dht11_sleep_time = 20

while True:
	# Reading serial
	try:
		data = se.readline()
		if data:
			data_clear = data.decode().split("|")
			date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			temperature = 0 # data_clear
			humidity = 0 # data_clear
			mq2 = 0 # data_clear
			dht11_th = Thread(target=insert_from_serial, args=(temperature, humidity, None, dht11_sleep_time, ), name="DHT11-Thread")
			dht11_th.start()
			mq2_th = Thread(target=insert_from_serial, args=(None, None, mq2, mq2_sleep_time, ), name="MQ2-Thread")
			mq2_th.start()
	except Exception as err:
		print(f"Ocorreu um problema: {err}")
