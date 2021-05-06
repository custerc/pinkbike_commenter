import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# read the data into a df
df = pd.read_csv('C:/Users/custerc/pinkbike_project/data/pb_comments.csv')
# convert df to list of lists
data = df.values.tolist()

# create analyzer
analyzer = SentimentIntensityAnalyzer()

# function for getting compount score from a comment


def get_score(comment):
    score = analyzer.polarity_scores(comment)['compound']
    return score


# get scores for each comment
for row in data:
    comment_text = row[2]
    vader_compound_score = get_score(comment_text)
    row.append(vader_compound_score)

# back into pandas we go
df = pd.DataFrame(data, columns=['ignore_this', 'date', 'comment_text',
                  'upvotes', 'downvotes', 'title', 'vader_score'])
# create a new column called extreme when comment scores are over or under .5/-.5
df['extreme'] = np.where((df['vader_score'] <= 0.5) & (df['vader_score'] >= -0.5), False, True)
# get a df of just those extreme comments
extreme_comments = df[df['extreme'] == True]
# save that column as a text file
# we'll use this file to train our model
extreme_comments['comment_text'].to_csv('pb_extreme_comments.txt', sep=' ', index=False)


# next step, use this to train model: https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce
# faster than doing it locally!
