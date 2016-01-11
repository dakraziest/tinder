import requests
import json
import threading

from . import constants
from . import errors

class Tinder(object):
	def __init__(self):
		self._session = requests.Session()
		self._session.headers.update(constants.HEADERS)
		self._token = None
		
	def _url(self,path):
		return constants.URL + path

	#gets the token and adds it to the header
	def auth(self, fb_auth_token, fb_user_id):
		data = json.dumps({'facebook_token': fb_auth_token, 'facebook_id': str(fb_user_id)})
		result = self._session.post(self._url('/auth'), data = data).json()
		if 'token' not in result:
			raise errors.RequestError(result)
		self._token = result['token']
		self._session.headers.update({"X-Auth-Token": str(result['token'])})
		return result

	def _request(self, method, url, data={}):
		if not hasattr(self, '_token'):
			raise errors.RequestError("Token not found")
		result = self._session.request(method, self._url(url), data=json.dumps(data))
		#Too many requests, wait and try again
		while result.status_code == 429:
			blocker = threading.Event()
			blocker.wait(0.01)
			result = self._session.request(method, self._url(url), data=json.dumps(data))
		if result.status_code != 200:
			raise errors.RequestError(result.status_code)
		return result.json()

	def _get(self, url):
		return self._request("get", url)

	def _post(self, url, data={}):
		return self._request("post", url, data=data)

	def _get(self, url):
		return self._request("get", url)

	def _post(self, url, data={}):
		return self._request("post", url, data=data)

	def updates(self):
		return self._post("/updates")

	def meta(self):
		return self._get("/meta")

	def recs(self):
		return self._get("/user/recs")

	def matches(self):
		return self.updates()['matches']

	def profile(self):
		return self._get("/profile")

	def update_profile(self, profile):
		return self._post("/profile", profile)

	def like(self, user):
		return self._get("/like/{}".format(user))

	def dislike(self, user):
		return self._get("/pass/{}".format(user))

	def message(self, user, body):
		return self._post("/user/matches/{}".format(user),
						  {"message": str(body)})

	def report(self, user, cause=1):
		return self._post("/report/" + user, {"cause": cause})

	def user_info(self, user_id):
		return self._get("/user/"+user_id)

	def ping(self, lat, lon):
		return self._post("/user/ping", {"lat": lat, "lon": lon})

