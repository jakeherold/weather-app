import sqlite3
import time

# Connect to sqlite and create db if it doesn't exist
conn = sqlite3.connect('weather.db')
c = conn.cursor()


# Faux data for entry
# ts is timestamp in epoch
# We're declaring it as 
ts = int(time.time())
temp_k = 256.4

# Create Table
c.execute("""CREATE TABLE if not exists weather(
            epoch_time interger,
            temp_k real
)""")


# Write data to table
c.execute("INSERT INTO weather VALUES (:epoch_time, :temp_k)",{'epoch_time': ts, 'temp_k':temp_k,} )
conn.commit()

# Read Data from table
c.execute("SELECT * FROM weather")
print(c.fetchall())

# Trying to figure out how to tell if table exists. Trying in create method for now.
# c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{weather}';")
# print(c.fetchall())

# Delete Old rows (for updates to data, so we don't let the DB grow too big)

c.execute("DELETE FROM weather WHERE epoch_time < ?", (ts,))
conn.commit()

c.execute("SELECT * FROM weather")
print(c.fetchall())

conn.close()