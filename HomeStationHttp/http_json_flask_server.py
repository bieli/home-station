from flask import json, Flask

app = Flask(__name__)


@app.route('/api/v1/addrecord/1', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8887)

