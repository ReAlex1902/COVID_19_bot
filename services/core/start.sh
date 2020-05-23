#!/bin/sh

# Flask configuration
export FLASK_ENV=development # To enable or disable displaying errors
export FLASK_PORT=3000 # A port Flask is listening on. It must be the same port which is set for the docker container
export MYSQL_HOST='localhost'
export MYSQL_USER=root
export MYSQL_PASSWORD=test12
export MYSQL_DB=RedCross

# Running our app
python app.py


