import tweepy
import time
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime


my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
 "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}

auth = tweepy.OAuthHandler("YOS0DjxdDN3JcVZWSM8fzlrOQ", "dAt2hhJgV5M06BiOPZRxxEtEnMU85oOWF1CN8tpD3xsFolfnmN")
auth.set_access_token("1046043340196761602-JILFVkGovrZgVXNXoJmqMz1yAbLydI", "CjYSI8CfilrWfdj4cBN3lEKxzT7eAkfdLdWnfhkHy9gL1")

api = tweepy.API(auth)


while(True):

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    page = requests.get("https://abcnews.go.com/Elections/2020-us-presidential-election-results-live-map/")

    soup = BeautifulSoup(page.content, 'html.parser')

    sources = "Data from @ABC"
    
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    a = "#PresidentialElection results as of " +  d2 +  ", " + current_time + ":" + "\n" + "\n"

    ### POPULAR VOTE
    bidenVotes = soup.find('div', {'class':'PopVote PopVote--democrats'})
    trumpVotes = soup.find('div', {'class':'PopVote PopVote--republicans PopVote--rightAligned'})

    ### ELECTORAL VOTES
    trumpClass = soup.find('div', {'class':'Candidate Candidate--republican Candidate--rightAligned'})
    trumpElectoralVotes = trumpClass.find('div', {'class':'Candidate__Votes'})

    bidenClass = soup.find('div', {'class':'Candidate Candidate--democrat'})
    bidenElectoralVotes = bidenClass.find('div', {'class':'Candidate__Votes'})

    b = a + "Trump Popular Votes: " + trumpVotes.text + "\n" + "Trump Electoral Votes: " + trumpElectoralVotes.text + "\n \n" + "Biden Popular Votes: " + bidenVotes.text + "\n" "Biden Electoral Votes: " + bidenElectoralVotes.text +  "\n" + "\n" + sources + "\n"
    api.update_status(b)
    print(a)
    print("TWEETED")
    time.sleep(300)