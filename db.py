import sqlite3

# Connect to the database
conn = sqlite3.connect('prescription_hashes.db')
c = conn.cursor()

# Create a table to store prescription hashes
c.execute('''CREATE TABLE IF NOT EXISTS prescription_hashes (hash TEXT PRIMARY KEY)''')

# Commit and close the connection
conn.commit()
conn.close()
