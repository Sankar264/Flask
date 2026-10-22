from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def collect_signup_data():
    username = request.form.get('username')
    email = request.form.get('email')
    address = request.form.get('address')
    password = request.form.get('password')

    # Demo only: do not store or display passwords in a real application.
    return render_template(
        'success.html',
        username=username,
        email=email,
        address=address
    )

if __name__ == '__main__':
    app.run(debug=True, port=5002)
