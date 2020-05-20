#!/bin/sh

# Flask configuration
export FLASK_ENV=production # To hide errors from a user
export FLASK_PORT=3000 # A port Flask is listening on. It must be the same port which is set for the docker container

# Running our app
python ../app.py


