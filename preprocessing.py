import glob
import pandas as pd

# read all csv files in the current directory other than 'data.csv'
files = glob.glob('*.csv')
if 'data.csv' in files: files.remove('data.csv')
dfs = []
for file in files: dfs.append(pd.read_csv(file))

# combine all data frames
df = pd.concat(dfs, ignore_index=True)

df['tweets'].str.replace('\n', ' ')

# get new features and output to 'data.csv'
df.assign(uppercase_ratio = [sum([c.isupper() for c in tweet]) * 1.0 / len(tweet) for tweet in df['tweets']],
				exclamation_number = [sum([c == '!' for c in tweet]) for tweet in df['tweets']],
				question_number = [sum([c == '?' for c in tweet]) for tweet in df['tweets']],
				length = [len(tweet) for tweet in df['tweets']]).to_csv("data.csv", index=False)
