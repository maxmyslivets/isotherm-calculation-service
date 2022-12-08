# run flask server
s:
	flask --app server --debug run -h localhost -p 3000

# run flask client for test
c:
	py cl.py

# run flask server for upload file from web-page
ex:
	flask --app example_page run -h localhost -p 3001

# TODO: create tests for rest-api with pytest
