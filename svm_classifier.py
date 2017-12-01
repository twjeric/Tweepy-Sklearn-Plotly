import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from svmutil import *

if __name__ == '__main__':

    # Read Corpus
    df = pd.read_csv('data_with_nlp.csv', error_bad_lines=False)
    df = df.dropna()
    df = shuffle(df, random_state=97).reset_index(drop=True)

    # Select Features
    data_X = df[['user_friends_count', 'user_followers_count', 'retweet_count', 'exclamation_number', 'length',
                 'question_number', 'uppercase_ratio', 'nlppred']].values
    data_Y = df['happiness_index'].values

    # Random oversampling
    ros = RandomOverSampler()
    X_resampled, Y_resampled = ros.fit_sample(data_X, data_Y)

    # Standardization, optional
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

        model = svm_train(train_label.tolist(), train_feature.tolist(), '-c 4 -q')  # train the svm
        p_label, p_acc, p_val = svm_predict(test_label.tolist(), test_feature.tolist(), model)  # predict on test set
        accuracy.append(p_acc[0])

    print('10-CV Accuracy = {}'.format(np.mean(accuracy)))

    final_model = svm_train(Y_resampled.tolist(), X_resampled.tolist(), '-c 4 -q')  # train the final svm
    svm_save_model('happiness_index_svm.model', final_model)

