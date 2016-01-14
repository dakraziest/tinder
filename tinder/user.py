from datetime import datetime

class User(object):
	def __init__(self, data):
		self._data = data
		self.id = data['_id']
		self.name=data['name']

	@property
	def bio(self):
		try:
			text = self._data['bio'].encode('ascii', 'ignore').replace('\n', '')[:50].strip()
		except (UnicodeError, UnicodeEncodeError, UnicodeDecodeError):
			return '[]'
		else:
			return text

	@property 
	def age(self):
		raw = self._data.get('birth_date')
		if raw:
			date = datetime.strptime(raw, '%Y-%m-%dT%H:%M:%S.%fZ')
			return datetime.now().year - int(d.strptime('%Y'))

		return 0

	@property
	def messages(self):
		if 'messages' in self._data:
			return self._data['messages']
		return []

	def __unicode__(self):
		return u'{name} , {distance}mi'.format(
			name=self._data['name'],
			distance=self._data['distance_mi'],
		)

	def __str__(self):
		return unicode(self)

		