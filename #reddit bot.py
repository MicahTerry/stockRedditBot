#reddit bot
import praw
import random
reddit = praw.Reddit(
    client_id='IaHf4UEcrETF114iAGgajg',
    client_secret="zW1sK275kQ33PQbnC9XkRSehS7T8Qw",
    user_agent="<console:Micah's Bot:1.0>",
    username = "myredditbotttt",
    password = "jevgiv-bajpe1-cahdiJ"
)
polsubreddit = reddit.subreddit("Politics")
ukraine_suport = ["slava ukraini", "Putin is such a clown", "The Ukrainians are a brave people"]
for submission in polsubreddit.hot(limit=10):
    #print("*******")
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " ukraine " in comment_lower:
                print('--------')
                print(comment.body)
                random_index = random.randint(0, len(ukraine_suport)-1)
                comment.reply(ukraine_suport[random_index])



            