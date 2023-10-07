import hashlib
import json
import sqlite3

# Sample prescription data (replace this with your actual data)
prescription_data = {
    "patient_name": "John Doe",
    "age": 35,
    "date": "2023-08-25",
    "medicines": ["Medicine A", "Medicine B"],
    "quantity": [2, 1],
    "doctor_name": "Dr. Smith"
}

# Convert dictionary to JSON string
prescription_json = json.dumps(prescription_data, sort_keys=True)

# Create a hash of the prescription data
hash_object = hashlib.sha256(prescription_json.encode())
prescription_hash = hash_object.hexdigest()

# Connect to the database
conn = sqlite3.connect('prescription_hashes.db')
c = conn.cursor()

# Check if the prescription hash is in the database
c.execute('''SELECT * FROM prescription_hashes WHERE hash = ?''', (prescription_hash,))
existing_hash = c.fetchone()

if existing_hash:
    print("This prescription has already been used.")
else:
    # Store the prescription hash in the database
    c.execute('''INSERT INTO prescription_hashes (hash) VALUES (?)''', (prescription_hash,))
    print("Prescription Hash stored successfully.")

# Commit and close the connection
conn.commit()
conn.close()
