from datetime import datetime

class User(object):
	def __init__(self, data):
		self.data = data

	@property
	def id(self):
		return self.data['_id']

	@property
	def bio(self):
		try:
			text = self.data['bio'].encode('ascii', 'ignore').replace('\n', '')[:50].strip()
		except (UnicodeError, UnicodeEncodeError, UnicodeDecodeError):
			return '[]'
		else:
			return text

	def __unicode__(self):
		return u'{name} , {distance}mi'.format(
			name=self.data['name'],
			distance=self.data['distance_mi'],
		)

	def __str__(self):
		return unicode(self)

		