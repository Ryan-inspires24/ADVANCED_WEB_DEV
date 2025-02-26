import mysql.connector
conn = mysql.connector.connect(host="localhost", user="ryan_inspires", password="Asherinyuy24", database="wed_directory_listings_db")
cursor= conn.cursor()

sql = 'SELECT * FROM listing'
cursor.execute(sql)
listings = cursor.fetchall()


print(listings)