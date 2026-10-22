from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

# Task 1: Home and About navigation using url_for()
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Task 2: GET request - retrieve name and batchno from query parameters
@app.route('/student', methods=['GET'])
def get_student():
    name = request.args.get('name')
    batchno = request.args.get('batchno')

    return jsonify({
        'name': name,
        'batchno': batchno
    })


# Task 3: POST request - retrieve name and skills from JSON body
@app.route('/skills', methods=['POST'])
def get_skills():
    data = request.get_json(silent=True) or {}

    name = data.get('name')
    skills = data.get('skills')

    return jsonify({
        'name': name,
        'skills': skills
    })


if __name__ == '__main__':
    app.run(debug=True, port=5003)
