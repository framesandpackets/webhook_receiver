from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def base():
    return 'For receiver send POST to /receiver/ '

@app.route('/receiver', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == "application/json":
        get_info = json.dumps(request.json)
        print (get_info)
        return get_info

if __name__ == '__main__':
    app.run(debug=True)
