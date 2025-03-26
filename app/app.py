from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Mundo Desde Flask!!!!"

@app.route("/hora")
def hora():
    return f"La Hora Actual Es: {datetime.now()}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
