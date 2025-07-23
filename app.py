from flask import Flask, render_template
from bot_logic import fetch_ohlcv, check_signal

app = Flask(__name__)

@app.route('/')
def index():
    df = fetch_ohlcv()
    signal = check_signal(df)
    return render_template("index.html", signal=signal, tables=[df.tail().to_html(classes='data')])

if __name__ == '__main__':
    app.run(debug=True)
