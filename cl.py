import requests

url = 'http://127.0.0.1:3000/im_size'
my_img = {'image': open('E:/Wall.jpg', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())
