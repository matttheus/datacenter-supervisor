import psycopg2
import serial
import io
from time import time

# ENVIRONMENT VARIABLES
db_config = {
	'DATABASE': 'datacentersupervisor',
	'USER': 'postgres',
	'HOST': 'localhost',
	'PASSWORD': 'postgres',
}


# Make connection with the database
def db_connect(db_config):
	con_str = f"dbname={db_config['DATABASE']} user={db_config['USER']} host={db_config['HOST']} password={db_config['PASSWORD']}"
	con = psycopg2.connect(con_str) 
	cursor = con.cursor()

	return con, cursor


# Verify if the database exist
def db_exist(dbname):
   exist = False
   
   try:
      con, cursor = db_connect()
      cursor.execute(f"SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='{dbname}');")
      exist = cursor.fetchone()[0]
      cursor.close()
   except psycopg2.Error as e:
      print(e)

   return exist


def create_db(dbname):
	if db_exist(dbname):
		print('There is a database')
		return db_connect(db_config)
	else:
		print(f'There is no database with the name {dbname}, it will be created.')
		# NEW CONFIG
		_dbname = dbname
		_dbuser = input('Database user: ')
		_dbhost = input('Database host: ')
		_dbpassword = input('Database password: ')

		# ATT CONFIG
		db_config['DATABASE'] = _dbname
		db_config['USER'] = _dbuser
		db_config['HOST'] = _dbhost
		db_config['PASSWORD'] = _dbpassword

		# CREATE DATABASE
		from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
		con, cursor = db_connect(db_config)
		con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		cursor = conexao.cursor()
		cursor.execute(f"CREATE DATABASE {db_config['DATABASE']}")
		print('Database created')

		# CREATE TABLES
		con, cursor = db_connect(db_config)
		cursor.execute(f"CREATE TABLE temperature (id_temperature SERIAL PRIMARY KEY, value REAL, date_time TIMESTAMP);"
		+ f"CREATE TABLE humidity (id_humidity SERIAL PRIMARY KEY, value REAL, date_time TIMESTAMP);"
		+ f"CREATE TABLE gas (id_gas SERIAL PRIMARY KEY, value REAL, date_time TIMESTAMP);") 
					  
		con.commit()
		con.close()
		
		# CREATE CONNECTION
		print('Connetion created ...')
		return db_connect(db_config)


def insert_from_serial(value):
	con, cursor = db_connect(db_config)
	cursor.execute(f"INSERT INTO temperature(value) VALUES ({value});")
	con.commit()
	con.close()
	print('Insert accomplished!')


#---------------------------------------------------------------------
# Starting server
#---------------------------------------------------------------------

# print('Server started...')

# create_db('datacentersupervisor')
se = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
list = []
a = str(time())
tmp_now = a.split('.')[0]

while True:
	
	if not se.readline().decode('utf-8') == '':
		print(se.readline().decode('utf-8'))

	

# tmp_serial_data = 'FALTANDO CÓDIGO DO SERIAL'

# while True:
# 	insert_from_serial(serial_data)

# 	_serial_data = 'NOVO DADO DO SERIAL'

# 	if tmp_serial_data != _serial_data:
# 		tmp_serial_data = _serial_data