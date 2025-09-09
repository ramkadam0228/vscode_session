from flask import Flask, jsonify       
 
app=Flask(__name__)           
 
@app.route('/')               # single slash is main page
def welcome():
    return("Hello Welcome!")  

@app.route('/greet')               #Single slash and function name creates new page on UI
def greet():
    return("Hello greet!")  

@app.route('/greet1')               
def greet1():
    return("Learn Python")  

@app.route('/addition1')               
def addition1():
    a=10
    b=20
    c=a+b
    return(jsonify(c))  # by default flask return list/list/dictionary , it cannt return Int so we need to convert int into list
# this can also be achived by jsonify utility, which internally converts data type and do preety print
 


if __name__=="__main__":      
    app.run(host='0.0.0.0', port=5000, debug=True)       



  # we added new function call
# but we did not use debug=True
# if we dont close the session we will not able to check the second url      
