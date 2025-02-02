from flask import Flask
import json

app = Flask(__name__)


@app.route("/ping")
def ping():
    return json.dumps({"status": "success"})


if __name__ == "__main__":
    app.run()
