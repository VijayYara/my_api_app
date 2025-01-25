from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

marks_data = [{
        "name": "KXV",
        "marks": 27
    },
    {
        "name": "6LmFa",
        "marks": 25
    }]

# @app.route("/api", methods=["GET"])
@app.route("/api", methods=["GET"])
def get_marks():
    # Get the 'name' parameters from the query string
    names = request.args.getlist('name')
    
    # Fetch the marks for each name from the marks_data dictionary
    marks = [i['marks'] for i in marks_data if i['name'] in names]
    # marks = [123, 456]
    return jsonify({"marks": marks})
