import requests
from base64 import b64encode

url = 'http://127.0.0.1:3000/im_size'
with open('E:/Wall.jpg', 'rb') as file:
    binary_file = b64encode(file.read())
data = {'image': binary_file}
r = requests.post(url, data=data)

# convert server response into JSON format.
print(r.json())
