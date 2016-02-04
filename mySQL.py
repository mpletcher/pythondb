#!/usr/bin/python

# MySQL database using Python
# 1. Import db DATA created in mpletcher.com phpMyAdmin
# 2. Create a class to automatically setup db operations
# 3. Run queries and debug results

import MySQLdb

class Database:
	host	= "localhost"
	user	= "marcospletc12"
	passwd	= "mAnuc!ub6s@Ath"
	db 		= "DATA"

# Constructor that allows to connect to the db
def _init_(self):
	self.connection = MySQLdb.connect(	host = self.host, 
										user = self.user, 
										passwd = self.passwd,
										db = self.db)

# Class runs queries
def query(self, qr):
	cursor = self.connection.cursor( MySQLdb.cursors.DictCursor) # dict - accessible formate
	cursor.execut(qr) # executes variable that holds SQL content

	return cursor.fetchall() # returns all results

# Close and delele content in the class
def _del_(self):
	self.connection.close()

# Queries to give information back
if _name_ == "_main_":
	db = Database()

	qr = "DELETE FROM DATA"

	db.query(qr)

	qr = """
	INSERT INTO DATA
	('name', 'age')
	VALUES
	('Marcos', '29'),
	('Tim', '29'),
	('Kathy', '40'),
	('Linda', '50')
	"""

	db.query(qr)

	qr = """
	SELECT * FROM DATA
	WHERE age = 29
	"""

	people = db.query(qr) # assign a new variable bc there are more than one persom

	for person in people:
		print "Data found: %s " % person['name']
