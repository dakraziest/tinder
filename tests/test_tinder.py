from tinder.tinder import Tinder
from tinder.user import User

import unittest
import config

class TestTinder(unittest.TestCase):
	def setUp(self):
		self._api = Tinder()
		
		self._api.auth(config.FACEBOOK_TOKEN, config.FACEBOOK_ID)
		
	def test_update_location(self):
		lat = 41.881832
		lon = -87.623177
		print self._api.ping(lat, lon)

	def test_nearby_users(self):
		response = self._api.recs()
		if 'results' in response:
			users = response['results']
			for user in users:
				print unicode(User(user))


if __name__ == '__main__':
	unittest.main()
