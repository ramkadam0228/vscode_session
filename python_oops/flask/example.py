from flask import Flask        # step-1: import the packages
 
app=Flask(__name__)            # step-2: create the instance of Flask class
 
@app.route('/')                # step-3: add the decorator above the function call
def welcome():
    return("Hello Welcome!")  # step-4: instead of print use return
 
if __name__=="__main__":      #step-5: block use to run the script as standalone
    app.run(debug=True)       #step-6: live code reloading

    #Host : 127.0.0.1 --> Local host
    # Port: default port: 5000  Local host means its only accessible from local machine