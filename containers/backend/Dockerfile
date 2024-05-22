FROM python:3.10-bookworm

SHELL ["/bin/bash", "-c"]
WORKDIR /app

RUN apt-get update && apt-get -y install git cron

RUN git clone https://github.com/The-Alpha-Project/Alpha-archives-website
WORKDIR /app/Alpha-archives-website/backend
RUN pip3 install -r requirements.txt && pip3 install mysql-connector-python==8.0.32 gunicorn mysqlclient

COPY configs/settings.py /app/Alpha-archives-website/backend/config
COPY configs/config.py /app/Alpha-archives-website/backend/utils/database_builder

COPY containers/backend/entry.sh containers/backend/wait_for_db.py containers/backend/insert_user.py /
RUN chmod +x /entry.sh

ENTRYPOINT [ "/entry.sh" ]