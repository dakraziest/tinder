#Documentation

```python
import tinder

#create new session
session = tinder.Session(facebook_id, facebook_token)

session.matches() #an array of User that you have matched with

session.recommendations() #an array of User to like or nope
```
The user class has the following properties:

 * id
 * bio
 * *more coming soon*

```python

#like a user
session.like(user_id)

#nope a user
session.nope(user_id)

#message a user
session.message(user_id, body)

#unmatch a user
session.delete(user_id)

#update location 
session.update_location(latitude, longitude)

#update bio
session.update_bio(bio)
```

