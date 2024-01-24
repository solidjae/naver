import psycopg2
import json 
from datetime import datetime

def parse_data(json):
    date_of_parse = datetime.now().date()

    params = {
        "host": "sofsys.postgres.database.azure.com",
        "dbname": "postgres", 
        "user": "sofsys",
        "password": "withus4u!"
    }   
    
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    interactions_by_channel = json['numInteractionsByChannel']

    for item in interactions_by_channel:
        cur.execute("INSERT INTO naver_daily_interactions_by_channel (date, dimension, metric) VALUES (%s, %s, %s)", (date_of_parse, item['dimension'], item['metric']))
    
    cur.execute("INSERT INTO naver_daily_interactions_by_channel (date, total) VALUES (%s, %s)", (date_of_parse, json['numInteraction'],))



    conn.commit()
    cur.close()
    conn.close()

