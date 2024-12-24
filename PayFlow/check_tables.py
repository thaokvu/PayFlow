import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payroll.db')
cursor = conn.cursor()

# Create the payroll table
cursor.execute('''
CREATE TABLE IF NOT EXISTS payroll (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    salary REAL NOT NULL,
    tax_deductions REAL NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Payroll table created (if it did not already exist).")

