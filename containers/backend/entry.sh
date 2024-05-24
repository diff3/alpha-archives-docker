#!/bin/bash

DIRECTORY="/app/Alpha-archives-website/backend/media/Alpha-Project-Archive"

python /wait_for_db.py

if [ ! -f /etc/configured ]; then
    # if [ -d "$DIRECTORY" ]; then
       # echo "Directory $DIRECTORY exists."
    # else
        # echo "Directory $DIRECTORY does not exist. Cloning repository..."
        # git clone https://github.com/The-Alpha-Project/Alpha-Project-Archive "$DIRECTORY"
    # fi

    cd /app/Alpha-archives-website/backend
    python manage.py makemigrations && python manage.py migrate
    python /insert_user.py
    cd utils/database_builder && python main.py

    service cron start
    touch /etc/configured
fi
    
cd /app/Alpha-archives-website/backend && gunicorn --bind 0.0.0.0:8000 config.wsgi:application
# cd /app/Alpha-archives-website/backend && python manage.py runserver
