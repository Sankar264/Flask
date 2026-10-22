from flask import Flask,redirect,render_template,url_for,request
#create a flask application instance
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

#name = ekanth,email = ekanth@gmail.com
@app.route('/getData',methods=['GET'])
def getData():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'The name is {name} and email is {email}'

'''
@app.route('/postData',methods=['POST'])
def postData():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'The name is {name} and email is {email}'
'''

@app.route('/postData',methods=['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name)<5:
        return render_template('index.html',
                               err="Invalid name")
    if email is None:
            return render_template('index.html',
                                   err="Invalid email")
    if password is None or len(password)<8:
            return render_template('index.html',
                                   err="password is wrong")
    return render_template('index.html',msg = "success")

@app.route('/updateData/<email>',methods=['PUT'])
def updateData(email):
    data = request.get_json()
    email1 = data['email']
    print(email1)
    #DATABASE LOGIC for PUT
    return f"Data is updated Successfully for {email}"

@app.route('/deleteData/<email>',methods=['DELETE'])
def deleteData(email):
    #DATABASE Logic for Delete
    return f"Data is deleted successfully for {email}"

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
        name = request.args.get('name')
    if request.method == "POST":
        data = request.get_json()
        name = data['name']
    return f'The name is {name}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5100,debug=True)
    