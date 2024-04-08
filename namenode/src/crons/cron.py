from datetime import datetime, timedelta
from src.database.database import connect
from src.replication_manager import handle_replication
import schedule
import time
import logging

# Configura el logging para que puedas ver la salida en la consola y en un archivo
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='namenode_cron.log', filemode='a')

def job():
    now = datetime.now()
    minute_ago = now - timedelta(minutes=1)
    client, collection = connect("node")
    
    try:
        query = {"status": True, "last_heartbeat": {"$lt": minute_ago}}
        nodes_down = list(collection.find(query))
        
        if nodes_down:
            collection.update_many(query, {"$set": {"status": False}})
            for node_down in nodes_down:
                handle_replication(node_down["_id"])
                logging.info(f"Replication triggered for node: {node_down['_id']}")
    
    except Exception as e:
        logging.error(f"Error during cron job execution: {e}")
    finally:
        client.close()

schedule.every().minute.do(job)

def run_cron():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_cron()
