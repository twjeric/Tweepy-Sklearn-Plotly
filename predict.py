import pandas as pd
import pickle
import xgboost as xgb

with open('XGB.model', "r") as fp:
    clf = pickle.load(fp)

data = pd.read_csv('./test_trump_nlp.csv', error_bad_lines=False)
data = data.dropna()
result = data[['created_at']]
result.rename(columns = {'created_at':'dateTime'}, inplace=True)
data = data[['user_friends_count', 'user_followers_count', 'retweet_count', 'exclamation_number', 'length', 'question_number', 'uppercase_ratio', 'nlppred']]
data['retweet_count'] = pd.to_numeric(data['retweet_count'])

predictions = clf.predict(data) - 2

result['prediction'] = predictions
result['prediction'] = result['prediction'].astype(int)
result.to_csv('result.csv', index=False)

