import mysql.connector
import logging

def connect_to_db(db_config):
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
            charset='utf8mb4'
        )
        logging.info("Good conn")
        return conn
    except mysql.connector.Error as err:
        logging.error("Error conn")
        raise
    
def connect_databases(config):
    xenforo_conn = connect_to_db(config["xenforo_db"])
    return xenforo_conn