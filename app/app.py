from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola mundo desde Flask!"

@app.route("/hora")
def hora():
    return f"La hora actual es: {datetime.now()}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
