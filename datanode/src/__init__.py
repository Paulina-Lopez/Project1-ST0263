from src.crons.cron import run_cron
import threading

cron_thread = threading.Thread(target=run_cron)
cron_thread.start()
