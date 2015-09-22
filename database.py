import sqlite3 as lite
import pandas as pd
import sys

month = raw_input("Please state the month of interest ")

print month

con = lite.connect('getting_started.db')

with con: 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities;")
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("DROP TABLE IF EXISTS cities2;")
	cur.execute("DROP TABLE IF EXISTS weather2;")
	cur.execute("CREATE TABLE cities(name text, state text);")
	cur.execute("CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer);")

cities = (('New York City', 'NY'), 
('Boston', 'MA'),
('Chicago', 'IL'),
('Miami', 'FL'),
('Dallas', 'TX'),
('Seattle', 'WA'),
('Portland', 'OR'),
('San Francisco', 'CA'),
('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', '62'),
('Boston', 2013, 'July', 'January', 59),
('Chicago', 2013, 'July', 'January', 59),
('Miami', 2013, 'August', 'January', 84),
('Dallas', 2013, 'July', 'January', 77),
('Portland', 2013, 'July', 'December', 63),
('Seattle', 2013, 'July', 'January', 61), 
('San Francisco', 2013, 'September', 'December', 64),
('Los Angeles', 2013, 'September', 'December', 75))

with con:
	cur = con.cursor()
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

with con:
	cur = con.cursor()
	cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name = city WHERE warm_month=?",  (month,))
	rows = cur.fetchall()
	dataframe = pd.DataFrame(rows)

