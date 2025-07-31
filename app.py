from flask import Flask, render_template
from bot_logic import fetch_ohlcv, check_signal
import threading
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Load .env for shutdown time
load_dotenv()

app = Flask(__name__)

# Get shutdown time from .env or fallback
SHUTDOWN_TIME = os.getenv("AUTO_SHUTDOWN_TIME", "23:45")  # e.g., "23:00"

@app.route('/')
def index():
    df = fetch_ohlcv()
    signal = check_signal(df)
    return render_template("index.html", signal=signal, tables=[df.tail().to_html(classes='data')])

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()

def auto_shutdown_loop():
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == SHUTDOWN_TIME:
            print(f"[AUTO] Shutting down at {now}")
            os._exit(0)
        time.sleep(30)

if __name__ == '__main__':
    # Start background auto-shutdown thread
    threading.Thread(target=auto_shutdown_loop, daemon=True).start()
    app.run(debug=True, host="0.0.0.0")
