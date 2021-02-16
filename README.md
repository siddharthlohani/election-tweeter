# election-tweeter
#### simple python web scraper that utilizes the twitter api to tweet live election data
#### check out my [twitter](https://twitter.com/sidlohani) to see this project working!
 
### usage:
####  - to use this program, clone the repo into a directory of your choice
####  - IMPORTANT: make sure you have all the dependencies installed or the program will not compile
####  - try running these commands in the command line to make sure you have all dependencies downloaded:

~~~
 => pip install bs4
 => pip install requests
 => pip install tweepy
~~~

####  - then, create a [twitter developer account](https://developer.twitter.com/en), and create a new app
####  - in the election.py file:

~~~
auth = tweepy.OAuthHandler("YOS0DjxdDN3JcVZWSM8fzlrOQ", "dAt2hhJgV5M06BiOPZRxxEtEnMU85oOWF1CN8tpD3xsFolfnmN")
auth.set_access_token("1046043340196761602-JILFVkGovrZgVXNXoJmqMz1yAbLydI", "CjYSI8CfilrWfdj4cBN3lEKxzT7eAkfdLdWnfhkHy9gL1")
~~~

####  - replace the strings in the code above with your own api and consumer keys and tokens (don't try to run it with my keys... i obviously regenerated them and these keys don't work anymore :))

####  - lastly, run the program either in an ide of your choice or in the command line:
~~~
python election.py
~~~

####  - enjoy!


## About:
#### hi, i'm sid! to see my other projects, visit my [website](http://siddharthlohani.dev/)!
