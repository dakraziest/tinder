from . import api
from . import user

class Session(object):

	def __init__(self, facebook_token, facebook_id):
		self._api = api.TinderAPI()
		self._api.auth(facebook_token, facebook_id)

	def recommendations(self):
		response = self._api.recs()
		users = []
		results = response['results']
		for result in results:
			yield user.User(result)

	def matches(self):
		for match in self._api.matches():
			yield user.User(match)

	def like(self, user_id):
		return self._api.like(user_id)

	def nope(self, user_id):
		return self._api.nope(user_id)

	def delete(self, user_id):
		return self._api._request('DELETE', 'user/matches/' + user_id)

	@property
	def profile(self):
		return self._api.profile()

	def message(self, user_id, body):
		return self._api.message(user_id, body)

	def update_location(self, lat, lon):
		return self._api.ping(lat, lon)

	def update_bio(self, bio):
		profile = {}
		profile['bio'] = bio
		return self._api.update_profile(profile)

