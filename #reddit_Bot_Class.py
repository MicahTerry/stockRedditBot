#reddit_Bot_Class
from unittest import defaultTestLoader
import praw
import pandas as pd
from yahoo_fin import stock_info as si
reddit = praw.Reddit(
    client_id='IaHf4UEcrETF114iAGgajg',
    client_secret="zW1sK275kQ33PQbnC9XkRSehS7T8Qw",
    user_agent="<console:Micah's Bot:1.0>",
    username = "myredditbotttt",
    password = "jevgiv-bajpe1-cahdiJ")
#polsubreddit = reddit.subreddit("Politics")


#gather tickers from major stock exchanges
df1 = pd.DataFrame (si.tickers_sp500())
df2 = pd.DataFrame (si.tickers_nasdaq())
df3 = pd.DataFrame (si.tickers_dow())
df4 = pd.DataFrame (si.tickers_other())

#convert dataframes to lists then to sets
sym1 = set(symbol for symbol in df1[0].values.tolist())
sym2 = set(symbol for symbol in df2[0].values.tolist())
sym3 = set(symbol for symbol in df3[0].values.tolist())
sym4 = set(symbol for symbol in df4[0].values.tolist())

#put all the sets together
symbols = set.union( sym1, sym2, sym3, sym4)

investingsubred = reddit.subreddit("Stocks")

ticker_dict ={}

for ticker in symbols:
    ticker_dict[ticker] = 0
#print("the length of the dictionary is",len(ticker_dict))

singleLetterDict = {}

for key,value in ticker_dict.items():
    if len(key) == 1:
        singleLetterDict[key]=value

for key in singleLetterDict.keys():
    if key in ticker_dict.keys():
        ticker_dict.pop(key)
ticker_dict.pop("")
#print(singleLetterDict)
#print("the length of the dictionary is",len(ticker_dict))
for submission in investingsubred.top(limit=10):
    numOfComments = 0
    for comment in submission.comments:
        if hasattr(comment, "body"):
            for ticker in ticker_dict:
                tick = " {} ".format(ticker)
                if tick in comment.body:
                    ticker_dict[ticker] +=1

#finished for the day, all that should be left is to return the keys with the highest values.
def findMostCommonStock(dict):
    biggestKey =[]
    biggestValue =0
    for key, value in dict.items():
       if value > biggestValue:
          biggestKey = key
          biggestValue = value
    return biggestKey, biggestValue
keys={}
for key, value in ticker_dict.items():
    if value > 5:
        keys[key]=value
print(keys)

print(ticker_dict['AAPL'])
print(findMostCommonStock(ticker_dict))

print("single letter dict",singleLetterDict)
max_key = max(ticker_dict)
max_value = max(ticker_dict.values())
#print(max_key, max_value)