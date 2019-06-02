import sqlite3
import time
import requests
import yaml
import json

with open("./secrets.yml") as y:
    token_string = yaml.safe_load(y)


api_address = "http://api.openweathermap.org/data/2.5/weather?id=4975802&appid={}".format(token_string['token'])
response = requests.get(api_address)
weather_json = response.json()
#print(response.status_code)
print(weather_json['main']['temp'])
#print(type(response.text))

# if response.status_code == 200:
#     print("API up: please continue")
# else: 
#     print("ABANDON THREAD! THIS STUFF'S BROKE!")







# Connect to sqlite and create db if it doesn't exist
conn = sqlite3.connect('weather.db')
c = conn.cursor()


# Faux data for entry
# ts is timestamp in epoch
ts = int(time.time())
temp_k = 256.4

# Create Table
c.execute("""CREATE TABLE if not exists weather(
            epoch_time interger,
            temp_k real
)""")

def update_weather_table(timestamp, temp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather VALUES (:epoch_time, :temp_k)",{'epoch_time': ts, 'temp_k':temp_k,} )
    conn.commit()
    conn.close()


def read_table_data ():
    # Read Data from table
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    print(c.fetchall())
    conn.close()



# Delete Old rows (for updates to data, so we don't let the DB grow too big)
def clean_old_table_data(timestamp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("DELETE FROM weather WHERE epoch_time < ?", (timestamp,))
    conn.commit()
    conn.close()



# read_table_data()
# update_weather_table(ts, temp_k)
# clean_old_table_data(ts)
# read_table_data()