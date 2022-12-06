import requests

url = 'http://127.0.0.1:5000/im_size'
my_img = {'image': open('E:/wall.jpg', 'rb')}
r = requests.post(url, files=my_img)
print(r)

# convert server response into JSON format.
print(r.json())
