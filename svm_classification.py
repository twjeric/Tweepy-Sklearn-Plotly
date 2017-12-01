import string
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from svmutil import *


# Apply Z-score Standardization to the data and return the standardized data
def z_score(data):
    dim = data.shape[1]  # dimension of features
    for i in range(dim):  # for every feature of the data
        col = data[:, i]
        col_mean = np.mean(col)  # mean of the feature
        col_std = np.std(col)  # standard deviation of the feature
        data[:, i] = (data[:, i] - col_mean) / col_std  # Apply Z-score Standardization
    return data


if __name__ == '__main__':
    class_num = 5
    count = [0] * class_num

    # Read Corpus
    df = pd.read_csv('data_with_nlp.csv', error_bad_lines=False)
    df = df.dropna()
    df = shuffle(df, random_state=97).reset_index(drop=True)

    # Data Preprocess
    data_X = df[['user_friends_count', 'user_followers_count', 'retweet_count', 'exclamation_number', 'length',
                 'question_number', 'uppercase_ratio', 'nlppred']].values
    # data_X = df[['user_friends_count', 'user_followers_count']].values
    data_Y = df['happiness_index'].values
    for y in data_Y:
        count[int(y)+2] += 1
    print(count)

    # Over sampling
    ros = RandomOverSampler()
    X_resampled, Y_resampled = ros.fit_sample(data_X, data_Y)
    count = [0] * class_num
    for y in Y_resampled:
        count[int(y)+2] += 1
    print(count)

    # X_resampled = z_score(X_resampled)

    # Standardization
    # scaler = StandardScaler()
    # scaler.fit(X_resampled)
    # X_resampled = scaler.transform(X_resampled)

    # 10-Fold cross validation
    hold = 10
    kf = KFold(n_splits=hold)
    accuracy = []
    for train_keys, test_keys in kf.split(range(len(X_resampled))):
        train_feature = X_resampled[train_keys]
        train_label = Y_resampled[train_keys]
        test_feature = X_resampled[test_keys]
        test_label = Y_resampled[test_keys]

        count = [0] * class_num
        for y in train_label:
            count[int(y) + 2] += 1
        print('train:', count)
        count = [0] * class_num
        for y in test_label:
            count[int(y) + 2] += 1
        print('test:', count)

        model = svm_train(train_label.tolist(), train_feature.tolist(), '-c 4 -q')
        p_label, p_acc, p_val = svm_predict(test_label.tolist(), test_feature.tolist(), model)
        accuracy.append(p_acc[0])

    print('10-CV Accuracy = {}'.format(np.mean(accuracy)))
    print(len(X_resampled))
