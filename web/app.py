from flask import Flask
import requests as r

app = Flask(__name__)


@app.route("/home")
def ping():
    response = r.get("http://server-cluster-ip-srv:8081/ping")
    return response.json()


if __name__ == "__main__":
    app.run()
