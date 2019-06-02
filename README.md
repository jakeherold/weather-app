# weather-app
A mini-weather API using Vagrant, Python, SQLite, and Puppet

# How to Use
* Get your local host machine set up with vagrant, to the point that you can set up a vagrant VM from a vagrantfile
* Clone this repo to your host machine
* Get free API key from https://home.openweathermap.org/
* Create a file called secrets.yml in the root of the repo directory. 
* Add a line to secrets.yml like this: token: '[token goes here]'
* Save secrets.yml
* vagrant up
* vagrant ssh
* sudo python /vagrant/weather_server.py

# To-Do List
* ~~Get basic DB functionality up~~
* ~~Get basic API call functionality up~~
* Get it to run on a vagrant server (been testing after various stages, but now need to finish validating that it still runs)
* Get REST API up and running. 
* True-up REST API function to Vagrant box
* Sort out puppet things

# Limitations
* API Timeout - No more than 60 per minute w/ my free tier API Token, with 95% uptime SLA

# Extension Ideas
* Play with in-memory DB, see if that's lighter and appropriate to the task
* How to lighten this repo

# Various notes and thoughts
* Vagrant is a really sweet tool. Regardless of how this project turns out I'm going to have to remember this one.
* Validated that the newest "build" of the wather_server.py script works on a fresh vagrant install (9:59am PST)
* So, now that i'm working on the API component of it, it's a little more tricky to get the appropriate env. set up on the vagrant VM. This is compounded by the fact that i'm not using shell scripts. I've opted for the workaround of using a few install lines in my vagrant file. Admittedly, I should find the .rpm files that i want, and keep those in this repo (or find a stable version), but since this is more POC than anything, I'm going to keep it a little hacky.
