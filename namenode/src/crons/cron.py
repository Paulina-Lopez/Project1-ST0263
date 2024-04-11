import schedule
import time
import logging
from datetime import datetime, timedelta
from ..replication_manager import handle_replication
from src.database.database import connect

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='namenode_cron.log', filemode='a')

def job():
    now = datetime.now()
    minute_ago = now - timedelta(seconds=30)
    client, collection = connect("node")
    try:
        query = {"status": True, "report_date": {"$lte": minute_ago}}
        nodes_query = collection.find(query)
        nodes_down = list(nodes_query)
        print(nodes_down)
        if nodes_down:
            collection.update_many(query, {"$set": {"status": False}})
            for node_down in nodes_down:
                handle_replication(node_down["_id"])
                logging.info(f"Replication triggered for node: {node_down['_id']}")
    
    except Exception as e:
        print(e)
    finally:
        client.close()
        print("Cron executed")

schedule.every().minute.do(job)

def run_cron():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_cron()