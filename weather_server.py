import sqlite3
import time
import requests
import yaml
import json

# Get secrets sorted locally
with open("./secrets.yml") as y:
    token_string = yaml.safe_load(y)

def k_to_f (temp_in_k):
    f = ((9/5)*(temp_in_k - 273) + 32)
    return round(f,2) # decimal place standard is based on what I get from the API (2 decimial places)

def update_weather_table(timestamp, temp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather VALUES (:epoch_time, :temp_f)",{'epoch_time': timestamp, 'temp_f':temp,} )
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

def database_check_or_create():
    # Connect to sqlite and create db if it doesn't exist
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE if not exists weather(
            epoch_time interger,
            temp_f real
    )""")
    conn.close()

def get_weather_from_api():
    api_address = "http://api.openweathermap.org/data/2.5/weather?id=4975802&appid={}".format(token_string['token'])
    response = requests.get(api_address)
    return dict(response.json())
    
    



# Faux data for entry
# ts is timestamp in epoch
ts = int(time.time())
jake = 56.76




database_check_or_create()
weather_json = get_weather_from_api()
read_table_data()
update_weather_table(ts, float(k_to_f(weather_json['main']['temp'])))
clean_old_table_data(ts)
read_table_data()


#print(weather_json)
#print("Portland Weather in Kelvin: " + str(weather_json['main']['temp']))
#print("Portland Weather in Fahrenheit: " + str(k_to_f(weather_json['main']['temp'])))