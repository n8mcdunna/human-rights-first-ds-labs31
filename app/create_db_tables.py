""" Initialize tables for Postgres database """
import psycopg2
import os
from dotenv import load_dotenv


def initialize_police_table():
    load_dotenv() 

    POLICE_TABLE = """CREATE TABLE IF NOT EXISTS police_force (
        id SERIAL PRIMARY KEY NOT NULL,
        dates TIMESTAMP,
        added_on TIMESTAMP,
        links TEXT,
        case_id TEXT,
        city TEXT,
        state TEXT,
        lat FLOAT,
        long FLOAT,
        title TEXT,
        description TEXT,
        tags TEXT,
        force_rank TEXT
    );"""
    
    TWITTER_TABLE = """CREATE TABLE IF NOT EXISTS twitter_potential_incidents (
        id_str TEXT,
        title TEXT,
        user_name TEXT,
        user_description TEXT,
        city TEXT,
        state TEXT,
        lat TEXT,
        long TEXT,
        category TEXT,
        language TEXT,
        created TEXT,
        source TEXT 
    )"""

    #Connect to DB and execute create table query
    db_url = os.getenv('DB_URL')
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(POLICE_TABLE)
    curs.execute(TWITTER_TABLE)
    conn.commit()
    curs.close()
    conn.close()
