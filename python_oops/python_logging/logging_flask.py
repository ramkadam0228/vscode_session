from flask import Flask,request,jsonify
import logging
 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(filename)s:%(lineno)d-%(message)s',
                    filename='app1.log',
                    filemode='w')  # if file not save force=True
 
app= Flask(__name__)
 
@app.route('/',methods=['GET'])
def home():
    logging.info("home url accessed")
    return jsonify(message='Welcome to the Flask app')
 
@app.route('/add',methods=['POST'])
def add_numbers():
    try:
        data=request.get_json()
        logging.debug(f"recieved: {data}")
 
        if 'a' not in data or 'b' not in data:
            logging.warning("Invalid request data : Missing 'a' or 'b' ")
            return jsonify(error="Missing 'a' or 'b'")
       
        a=data['a']
        b=data['b']
 
        c= a+b
        logging.info(f"Addition of {a} and {b} is:{c}")
        return jsonify(c)
   
    except Exception as e:
        logging.error(f"An error occured is : {e}")
        return jsonify("Internel server error")
   
@app.route('/critical',methods=['GET'])
def trigger_critical():
    logging.critical("some critical issue")
    return jsonify(message="A critical error occured!")
 
 
if __name__=="__main__":
    app.run(debug=True)
