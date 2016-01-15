#Documentation

```python
import tinder

#create new bot
bot = tinder.Bot(facebook_id, facebook_token)

bot.matches() #an array of User that you have matched with

bot.recommendations() #an array of User to like or nope
```
The user class has the following properties:

 * id
 * name
 * bio
 * messages
 * age
 * *more coming soon*

```python

#like a user
bot.like(user_id)

#nope a user
bot.nope(user_id)

#message a user
bot.message(user_id, body)

#unmatch a user
bot.delete(user_id)

#update location 
bot.update_location(latitude, longitude)

#update bio
bot.update_bio(bio)

#get profile information
print bot.profile #prints profile, kinda ugly
print bot.profile['bio'] #prints bio
print bot.profile['pos_info']['city']['name'] #prints name of current city
```

