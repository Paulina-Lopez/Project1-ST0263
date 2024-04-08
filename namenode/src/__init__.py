from flask import Flask
from src.routes.routes import routes
from src.crons.cron import run_cron
import threading


app = Flask(__name__)
app.register_blueprint(routes)

cron_thread = threading.Thread(target=run_cron)
cron_thread.start()