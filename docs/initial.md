# Isotherm calculation service

### Description .py files


#### _server.py_

Starting a server with a post-method on "http://127.0.0.1:3000/im_size", that takes file and return response in json-format
```json
{"msg": "success", "size": [1920, 1080]}
```


#### _cl.py_

Send file on "http://127.0.0.1:3000/im_size" and prints response


#### _example_page.py_

Starting a server with a web-page template on on "http://127.0.0.1:3001/" for upload file. Server saves file into local directory.
