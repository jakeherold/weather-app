# weather-app
A mini-weather API using Vagrant, Python, SQLite, and Puppet


# To-Do List
* Get basic DB functionality up (mostly done, may need cleanup)
* Get basic API call functionality up (got it up and running, need to connect it to DB functions now)
* Get it to run on a vagrant server
* Sort out puppet things

# Extension Ideas
* Play with in-memory DB, see if that's lighter and appropriate to the task
* How to lighten this repo

# Various notes and thoughts
* Vagrant is a really sweet tool. Regardless of how this project turns out I'm going to have to remember this one.
* Validated that the newest "build" of the wather_server.py script works on a fresh vagrant install (9:59am PST)
* So, now that i'm working on the API component of it, it's a little more tricky to get the appropriate env. set up on the vagrant VM. This is compounded by the fact that i'm not using shell scripts. I've opted for the workaround of using a few install lines in my vagrant file. Admittedly, I should find the .rpm files that i want, and keep those in this repo (or find a stable version), but since this is more POC than anything, I'm going to keep it a little hacky.
