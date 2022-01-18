### config.py ###
import psycopg2
# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

USER=''
PASSWORD=''
DATABASE_NAME=''
DATABASE_URL = f'postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432/{DATABASE_NAME}'