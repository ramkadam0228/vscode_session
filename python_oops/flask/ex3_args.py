from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/')
def welcome():
    return("Hello Welcome")

@app.route('/add1')
def add1():
    a=10
    b=20
    c=a+b
    return(jsonify(c))

@app.route('/add2')
def add2():
    # return("Enter first number for addition of 2 numbers")
    a=request.args.get('num1',type=int)  # By default the type is String
    # return("Enter Second number for addition of 2 numbers")
    b=request.args.get('num2',type=int)
    c=a+b
    return(jsonify(c))


@app.route('/user')  #http://127.0.0.1:5000/user1?name=kadam
def show_user():
    name=request.args.get('name')
    return (f"Hello {name}")

@app.route('/user1/<name>')  #http://127.0.0.1:5000/user1/kadam
def show_user1(name):
    # name=request.args.get('name')
    return (f"Hello {name}")

if __name__=="__main__":
    app.run(debug=True)
