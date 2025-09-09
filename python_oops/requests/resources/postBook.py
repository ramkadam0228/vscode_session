from payLoad import *

# import python_oops
# from python_oops.requests.resources.payLoad import addBookPayLoad
import requests
response_post=requests.post("http://216.10.245.166/Library/Addbook.php",json=addBookPayLoad("1111")
 
# "name":"Learn API Automation with Python",
# "isbn":"KADAM",
# "aisle":"008",
# "author":"Ram Kadam"
, headers={"Content-Type":"application/json;charset=UTF-8"},)

json_response=response_post.json()
print(response_post.json())


print(json_response['ID'])
id=json_response['ID']

delete_res=requests.post("http://216.10.245.166/Library/DeleteBook.php",json={"ID":id},headers={"Content-Type":"application/json;charset=UTF-8"})
print(delete_res.json())
print(delete_res)
msg = delete_res.json()
print(msg)
expected_msg= {'msg': 'book is successfully deleted'}
assert msg == expected_msg