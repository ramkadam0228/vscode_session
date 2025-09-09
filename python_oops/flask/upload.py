from flask import Flask,request,render_template
 
# app=Flask(__name__)
 
# @app.route("/",methods=['GET'])
# def home():
#     return render_template("upload.html")
 
# if __name__=="__main__":
#     app.run(debug=True)
# from flask import Flask,request,render
 
app=Flask(__name__)
 
@app.route("/",methods=['GET'])
def home():
    return render_template("upload.html")
 
@app.route("/",methods=['POST'])
def uploadfile():
    file=request.files["file"]
    print(file)
    file.save(file.filename)
    return(f"file {file.filename} uploaded successfully")
 
if __name__=="__main__":
    app.run(debug=True)
