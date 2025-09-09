from flask import Flask,render_template,request
app=Flask(__name__)
 
@app.route("/",methods=['GET'])
def calculator():
    result=""
    num1=request.form.get("num1",type=float)
    num2=request.form.get("num2",type=float)
    operation=request.form.get("operation")
    if operation=="add":
        result=num1+num2
 
    elif operation=="subtract":
        result=num1-num2
 
    elif operation=="multiply":
        result=num1*num2
 
    elif operation=="divide":
        result=num1+num2
 
    return render_template("calculator.html",result=result)
 
if __name__=="__main__":
    app.run(debug=True)