from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])
def rest_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3030)