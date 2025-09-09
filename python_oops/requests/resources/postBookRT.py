from payLoad import *
import configparser

import requests

from configurations import *
# config= getconfig
response_post = requests.post(getconfig()['API']['endpoint']+'/Library/Addbook.php',json=addBookPayLoad("333"),headers={"Content-Type":"application/json;charset=UTF-8"},)

json_response=response_post.json()
print(response_post.json())
print(json_response['ID'])

id=json_response['ID']

delete_res=requests.post("http://216.10.245.166/Library/DeleteBook.php",json={"ID":id},headers={"Content-Type":"application/json;charset=UTF-8"})
# print(delete_res.json())
# print(delete_res)
msg = delete_res.json()
# print(msg)
expected_msg= {'msg': 'book is successfully deleted'}
assert msg == expected_msg