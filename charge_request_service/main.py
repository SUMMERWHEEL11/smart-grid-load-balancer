
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LOAD_BALANCER_URL = 'http://load_balancer:6000'

@app.route('/charge', methods=['POST'])
def charge_request():
    data = request.json
    resp = requests.post(f"{LOAD_BALANCER_URL}/route", json=data)
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
