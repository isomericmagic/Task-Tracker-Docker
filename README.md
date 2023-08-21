# Task Tracker Docker
This is a dockerized version of a simple web app that I wrote at New Relic. New Relic support engineers work with a lot of different software languages, and oftentimes it can be helpful to be able to spin up an application with a New Relic agent attached to it without having to perform a lot of configuration tasks. This particular app utilizes flask and connects to a MongoDB database, and can be used to reproduce issues with the New Relic python agent and MongoDB. 

**Usage** \
You will need to install docker. Once that's done just download the files, open a terminal / command prompt and navigate to the Task-Tracker-Docker-main directory, and then run\
`docker compose up`\
or\
`docker compose up --build`\
if you want to rebuild the app and database containers from scratch. Then just navigate to the following url:\
http://127.0.0.1:5000/ \
in your browser and start adding tasks. To attach the New Relic python agent to the application, just uncomment the first 2 lines in the app.py file, add your license key to the newrelic.ini file and then just restart the app.\
Once you are finished, just run\
`docker compose down`\
to shut the containers down.