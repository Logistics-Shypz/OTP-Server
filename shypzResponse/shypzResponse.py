from flask import Response
import json
from flask.helpers import make_response


class ShypzResponse(Response):
	charset = 'utf-8'
	default_status = 200
	default_mimetype = 'text/html'

	def __init__(self,response=None, status=None, headers=None,mimetype=None, content_type='application/json', direct_passthrough=False,data=None):
		self.response = response
		self.status = status
		self.headers = headers
		self.mimetype = mimetype
		self.content_type = content_type
		self.direct_passthrough = direct_passthrough
		self.data = json.dumps(data)

	def createResponse(self):
		my_response = make_response()
		my_response.headers['test_otp'] = 'done'
		my_response.headers['Content_Type'] = self.response._get_content_type(self.content_type,ShypzResponse.charset)
		my_response.status = self.status
		my_response.mimetype = self.mimetype
		my_response.data = self.data
		return my_response