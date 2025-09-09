from flask import Flask, redirect,url_for
 
app=Flask(__name__)
 
@app.route('/')
def home():
    return("Wecolme to Home page")
 
@app.route('/page1')
def page1():
    return(redirect(url_for("page2")))
 
@app.route('/page1/page2')
def page2():
    return("you are in page2")
 
if __name__=="__main__":
    app.run(debug=True)