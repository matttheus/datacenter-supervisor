import psycopg2
import serial
import io
from time import sleep
from datetime import datetime
from random import randint

# Make connection with the database
def db_connect():
	con = psycopg2.connect("dbname=datacentersupervisor user=postgres host=localhost password=postgres") 
	cursor = con.cursor()

	return con, cursor


def insert_from_serial(table, temperature, humidity, gas, date):
	con, cursor = db_connect()
	table = table
	cursor.execute(f"INSERT INTO {table} (temperature, humidity, gas, date) VALUES ({temperature}, {humidity}, {gas}, '{date}');")
	con.commit()
	con.close()
	print('Insert accomplished!')


#---------------------------------------------------------------------
# Starting server
#---------------------------------------------------------------------

print('Server started...')
while 1:
	date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	insert_from_serial('main_collection', randint(1, 10), randint(1, 10), randint(1, 10), date)
	sleep(1)
''' 
# Serial code
se = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
list = []
a = str(time())
tmp_now = a.split('.')[0]

while True:
	if not se.readline().decode('utf-8') == '':
		print(se.readline().decode('utf-8'))
'''

# tmp_serial_data = 'FALTANDO CÓDIGO DO SERIAL'

# while True:
# 	insert_from_serial(serial_data)

# 	_serial_data = 'NOVO DADO DO SERIAL'

# 	if tmp_serial_data != _serial_data:
# 		tmp_serial_data = _serial_data

