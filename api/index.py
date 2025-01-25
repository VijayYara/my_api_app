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
    {
        "name": "KXV",
        "marks": 27
    },
    {
        "name": "6LmFa",
        "marks": 25
    },
    {
        "name": "6",
        "marks": 3
    },
    {
        "name": "Zb6P2",
        "marks": 59
    },
    {
        "name": "d5L",
        "marks": 54
    },
    {
        "name": "Orvc",
        "marks": 77
    },
    {
        "name": "Ke1mX",
        "marks": 65
    },
    {
        "name": "8",
        "marks": 3
    },
    {
        "name": "7",
        "marks": 23
    },
    {
        "name": "uP4cinPvd",
        "marks": 53
    },
    {
        "name": "a",
        "marks": 28
    },
    {
        "name": "G3m44jqz",
        "marks": 90
    },
    {
        "name": "e0Fra0zUjL",
        "marks": 22
    },
    {
        "name": "ZFQN",
        "marks": 37
    },
    {
        "name": "bYZNVmv",
        "marks": 45
    },
    {
        "name": "b",
        "marks": 7
    },
    {
        "name": "IvFXQoNFdr",
        "marks": 96
    },
    {
        "name": "ANXr",
        "marks": 87
    },
    {
        "name": "iLw",
        "marks": 39
    },
    {
        "name": "2GGN9b",
        "marks": 55
    },
    {
        "name": "5v1YTGw",
        "marks": 76
    },
    {
        "name": "wEVB6uf1",
        "marks": 9
    },
    {
        "name": "PxK6rI",
        "marks": 36
    },
    {
        "name": "0su",
        "marks": 43
    },
    {
        "name": "7ag99",
        "marks": 66
    },
    {
        "name": "XAMx",
        "marks": 2
    },
    {
        "name": "86PxToVcP",
        "marks": 23
    },
    {
        "name": "BDeJ",
        "marks": 19
    },
    {
        "name": "YlGC4y1m",
        "marks": 10
    },
    {
        "name": "TIztZhz",
        "marks": 35
    },
    {
        "name": "uGFu",
        "marks": 86
    },
    {
        "name": "DEN6Eo",
        "marks": 36
    },
    {
        "name": "4DFK",
        "marks": 39
    },
    {
        "name": "xpBGKx",
        "marks": 8
    },
    {
        "name": "LYPthOPKgp",
        "marks": 46
    },
    {
        "name": "9H",
        "marks": 82
    },
    {
        "name": "IXdouM7",
        "marks": 78
    },
    {
        "name": "j67LOno8A",
        "marks": 60
    },
    {
        "name": "wWE25n9TJC",
        "marks": 99
    },
    {
        "name": "1bx",
        "marks": 3
    },
    {
        "name": "gWb4",
        "marks": 73
    },
    {
        "name": "Jj6rZ",
        "marks": 43
    },
    {
        "name": "Un",
        "marks": 5
    },
    {
        "name": "qYR",
        "marks": 74
    },
    {
        "name": "EMslBoNCUB",
        "marks": 58
    },
    {
        "name": "WMOOHYMbr",
        "marks": 96
    },
    {
        "name": "IO",
        "marks": 66
    },
    {
        "name": "g5hT1fz",
        "marks": 21
    },
    {
        "name": "Rd6tT8EYD",
        "marks": 81
    },
    {
        "name": "lM2bEzZ0H",
        "marks": 0
    },
    {
        "name": "7NnyW1",
        "marks": 39
    },
    {
        "name": "suOuQh",
        "marks": 99
    },
    {
        "name": "JVfBG8",
        "marks": 18
    },
    {
        "name": "9lObItA6",
        "marks": 42
    },
    {
        "name": "KND",
        "marks": 81
    },
    {
        "name": "eghxXVH2r7",
        "marks": 77
    },
    {
        "name": "YSEiNqvM",
        "marks": 90
    },
    {
        "name": "8EtGjb2",
        "marks": 21
    },
    {
        "name": "A",
        "marks": 4
    },
    {
        "name": "JCUtx3qm",
        "marks": 59
    },
    {
        "name": "w3EqVt7",
        "marks": 45
    },
    {
        "name": "EoXqzAZgav",
        "marks": 90
    },
    {
        "name": "SpHcvTzAHr",
        "marks": 80
    },
    {
        "name": "PHYRNzqJ",
        "marks": 72
    },
    {
        "name": "fRn5qZITW",
        "marks": 5
    },
    {
        "name": "hjOp79B4",
        "marks": 21
    },
    {
        "name": "SX87",
        "marks": 95
    },
    {
        "name": "u",
        "marks": 39
    },
    {
        "name": "Lwk",
        "marks": 3
    },
    {
        "name": "ALxNgN0",
        "marks": 28
    },
    {
        "name": "PHfCTn",
        "marks": 54
    },
    {
        "name": "SQX8",
        "marks": 53
    },
    {
        "name": "Ho5ZHsa",
        "marks": 14
    },
    {
        "name": "w8oElH1Ih6",
        "marks": 70
    },
    {
        "name": "jHhUC",
        "marks": 96
    },
    {
        "name": "S8AvGstJ",
        "marks": 77
    },
    {
        "name": "1h",
        "marks": 20
    },
    {
        "name": "dUeM",
        "marks": 65
    },
    {
        "name": "aRNBe88j",
        "marks": 17
    },
    {
        "name": "PZf06GY0mz",
        "marks": 46
    },
    {
        "name": "kQN8j2yz",
        "marks": 53
    },
    {
        "name": "6xGx0Qil9g",
        "marks": 46
    },
    {
        "name": "00qWJ",
        "marks": 22
    },
    {
        "name": "ba5b9c8g",
        "marks": 86
    },
    {
        "name": "VPXUiv2",
        "marks": 1
    },
    {
        "name": "68",
        "marks": 20
    },
    {
        "name": "adlt6Ls0uh",
        "marks": 44
    },
    {
        "name": "f40MSyi",
        "marks": 91
    },
    {
        "name": "eq",
        "marks": 41
    },
    {
        "name": "uvdaXJt",
        "marks": 71
    },
    {
        "name": "4eAYV7",
        "marks": 73
    },
    {
        "name": "4wBVI",
        "marks": 7
    },
    {
        "name": "qb9aV84",
        "marks": 81
    },
    {
        "name": "k6C3aeP",
        "marks": 16
    },
    {
        "name": "wvitjikyD",
        "marks": 82
    },
    {
        "name": "6Jg",
        "marks": 1
    },
    {
        "name": "7Z",
        "marks": 57
    },
    {
        "name": "33THlU0",
        "marks": 60
    },
    {
        "name": "KMWZwLjJ",
        "marks": 12
    },
    {
        "name": "M9tTQ6fcQc",
        "marks": 56
    }
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
