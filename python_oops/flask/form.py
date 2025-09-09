from flask import Flask,request,render_template
 
app=Flask(__name__)
 
@app.route("/",methods=['GET'])
def home():
    return render_template("form.html")
 
 
@app.route('/',methods=['POST'])
def user():
    name=request.form.get("name")
    return(f"hello {name}")
 
if __name__=="__main__":
    app.run(debug=True)