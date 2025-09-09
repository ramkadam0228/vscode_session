import requests
 
#Define out API endpoint
# also make sure that API end point should be active
 
url="http://127.0.0.1:5000/add2?num1=100&num2=200"
 
#Define the params : it is a key:value pair so pass in a dictionary
params={"num1":100,"num2":200}
 
# get a request
response=requests.post(url,params=params)
 
if response.status_code==200:
    print("Resonse:",response.json())
else:
    print("It is failed with status code:",response.status_code)
 
 