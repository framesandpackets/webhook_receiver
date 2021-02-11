from flask import json, request, Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def base():
    return 'For receiver send POST to /receiver/ '

@app.route('/receiver', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == "application/json":
        get_info = jsonify(request.json)
        return get_info
        print (get_info)

if __name__ == '__main__':
    app.run(debug=True)
