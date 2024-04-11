import schedule
import time
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import variables

def job():
    url = 'http://localhost:5000/node-on'
    data = {
        'ip': variables.ip_grpc,
        'port': variables.port_grpc
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("POST Success")
    else:
        print("POST request failed:", response.status_code)
    print("Datanode cron executed")

schedule.every().seconds.do(job)

def run_cron():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_cron()