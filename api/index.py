from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes (allow requests from any origin)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

marks_data = [
    {"name":"KXV","marks":1},{"name":"e6L","marks":14},{"name":"FaPB6Ce","marks":95},{"name":"b6P2k","marks":98},{"name":"d5L","marks":20},{"name":"VOrvcv","marks":90},{"name":"Ke1mX","marks":43},{"name":"C8CC7Oy","marks":47},{"name":"P4cinPvd","marks":60},{"name":"DaRrG3","marks":73},{"name":"44jqz48","marks":93},{"name":"0Fra0","marks":18},{"name":"UjLOYZFQN","marks":72},{"name":"pbYZ","marks":84},{"name":"Vmv","marks":74},{"name":"EbE7I","marks":54},{"name":"FXQoNFdr","marks":44},{"name":"XANXr2OiLw","marks":68},{"name":"k2GG","marks":50},{"name":"9bi","marks":90},{"name":"5v1YTGw","marks":84},{"name":"wwEVB6uf","marks":19},{"name":"FfPxK6rIW","marks":30},{"name":"0su","marks":81},{"name":"a7ag9","marks":55},{"name":"pXXAMxB086","marks":91},{"name":"xTo","marks":18},{"name":"cPOU","marks":48},{"name":"D","marks":68},{"name":"JLvYl","marks":41},{"name":"C4","marks":69},{"name":"1mGqTIztZ","marks":74},{"name":"zWTuGF","marks":76},{"name":"1iDEN6Eo","marks":47},{"name":"V4DF","marks":42},{"name":"Yf","marks":38},{"name":"pBGKxF8L","marks":14},{"name":"PthO","marks":73},{"name":"Kgp","marks":71},{"name":"G9Hzr","marks":52},{"name":"Xd","marks":90},{"name":"uM7w3j6","marks":48},{"name":"LOno8Al8wW","marks":0},{"name":"2","marks":39},{"name":"n9TJC9R1bx","marks":34},{"name":"T","marks":96},{"name":"Wb4tdJ","marks":73},{"name":"6rZbHU","marks":45},{"name":"DQqYRu5","marks":90},{"name":"M","marks":78},{"name":"lBoNCUBk","marks":2},{"name":"WMOOHYMbr","marks":34},{"name":"KIOpmg5hT1","marks":13},{"name":"zN2Rd6","marks":7},{"name":"T8EYDyzl","marks":63},{"name":"2bE","marks":68},{"name":"Z0HAj7Nny","marks":45},{"name":"1Yks","marks":98},{"name":"OuQh9gJV","marks":43},{"name":"BG8Lu9","marks":34},{"name":"ObItA6a","marks":97},{"name":"KND","marks":91},{"name":"6eghxXVH2","marks":81},{"name":"7wuYSEiN","marks":60},{"name":"vM3r8Et","marks":58},{"name":"jb","marks":94},{"name":"NAACwJCUt","marks":4},{"name":"3qmkpw3E","marks":89},{"name":"Vt7c9Eo","marks":41},{"name":"qzAZ","marks":49},{"name":"av45Sp","marks":24},{"name":"cv","marks":16},{"name":"zAHr","marks":80},{"name":"sPHYRNzqJ","marks":77},{"name":"0fRn5qZI","marks":77},{"name":"WDvh","marks":56},{"name":"Op79B4","marks":73},{"name":"YSX","marks":57},{"name":"77EuYRLwkC","marks":55},{"name":"ALxNgN0","marks":59},{"name":"gPH","marks":82},{"name":"CTnhWS","marks":5},{"name":"X8h","marks":82},{"name":"Ho5ZHsa","marks":24},{"name":"8w","marks":95},{"name":"oElH1Ih6re","marks":14},{"name":"HhUC7t","marks":52},{"name":"8Av","marks":1},{"name":"st","marks":13},{"name":"wH","marks":95},{"name":"hMXdUeMot","marks":41},{"name":"RNBe8","marks":57},{"name":"jL4PZf06GY","marks":64},{"name":"mzcvkQN8j","marks":89},{"name":"yzh76xGx0","marks":89},{"name":"il9","marks":31},{"name":"da00qW","marks":11},{"name":"Os","marks":59},{"name":"a5b9c","marks":33},{"name":"g1qVPXUiv2","marks":84}
]

# with open('marks.json') as f:
#     marks_data = json.load(f)

# @app.route("/api", methods=["GET"])
@app.route("/api", methods=["GET"])
def get_marks():
    # Get the 'name' parameters from the query string
    names = request.args.getlist('name')
    
    # Fetch the marks for each name from the marks_data dictionary
    marks = [i['marks'] for j in names for i in marks_data if i['name'] == j]
    # marks = [123, 456]
    return jsonify({"marks": marks})


# from flask import Flask, request, jsonify, Response
# import requests

# app = Flask(__name__)

# @app.route("/api", methods=["GET"])
# def proxy():
#     url = request.args.get("url")
#     if not url:
#         return jsonify({"error": "Missing URL parameter"}), 400
    
#     try:
#         response = requests.get(url)
#         headers = {"Access-Control-Allow-Origin": "*"}
        
#         flask_response = Response(response.content, response.status_code, headers)
#         return flask_response
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
