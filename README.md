### SharkBot
  
This is a telegram bot, which uses key, value from a json file to reply and say funny phrases on any channel that
you want to add it...
This version runs on the official Brazilian [FreeNas](https://t.me/freenasbr) group on Telegram.

But this bot was firstly created to be a funny bot at [GaragemHacker Curitiba HackerSpace](http://garagemhacker.org) group.
The main objective here is implement some level of a decision tree which can be used to moderate  
users on a Telegram, but in a very funny way, with some jokes and clever phrases :stuck_out_tongue_winking_eye:. It can also,
reply users in a random way searching the context in phrases and say something that can match with  
it's own vocabulary.
I have also created some level of hysteresis, which is used to do not disturb with the same moderation  
pharse every time when some moderation was already been asked.  
  
### How to use
  
At the point, I'm writing this README this bot doesn't have yet a yaml file,(_which will be a very nice improvement on this bot_ ).  
So to use this bot you must set only two variables:  
  
`token` must be set to your bot token as a string.  
`myid` must be set with your bot id.  
  
You can also adjust the phrases and even create more vocabulary, by changing the file `phrases.json`

### Dependencies
 * python-telegram-bot
 
### To-Do
This tasks will create a very nice improvement on this bot.
- [ ] Migrate to python3.
- [ ] Import all configurations from an external config file
- [ ] Create a nice GoodBye for who is leaving the group.
- [ ] Save history as logs in public servers.
- [ ] Create a docker container. 

#### License  
GPL-v3  

### Author  
  
Igor Brandao [isca](isca.space)  
  
Hope you Enjoy this bot... :wink:  

_Isca disclaims all copyright interest in the program “shark.py” (which is a chatter bot) is written by Igor Brandao_  
  
