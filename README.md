# Tweepy-Sklearn-Plotly
Detect and predict happiness index for twitter users according to their tweets.

## ML.py
### Description
Conduct both linear regression and logistic regression on 'data.csv'.
### Requirements
numpy, pandas, imbalanced-learn, scikit-learn
### Input
The code reads 'data.csv' to train model and reads 'test.csv' to use the trained model for prediction.
### Output
By commenting/uncommenting, the coefficients, Mean Squared Error (MSE) and variance score of the linear regression, and the accuracy of the logistic regression of each fold during cross validation (CV) would be printed to the console, as well as the average MSE of the linear regression and the average accuracy of the logistic regression after 10-fold CV. In addition, the coefficients of both models used for prediction could be printed to the console. And predicted results could be saved to a new file 'predictions.csv'.
### Usage
There are two parts of the code. From the beginning to the k-fold cross validation loop, it is used for feature selection. First let *data_X* contain all 10 candidate features. Then use ```data_X = np.delete(data_X, np.s_[0], axis=1)``` to drop one feature. Change the value of the parameter in *np.s_[]* to drop different features. The code after k-fold cross validation loop is used for prediction. 

## train.py
### Description
Conduct XGBoost (https://xgboost.readthedocs.io/en/latest/).
### Requirements
numpy, pandas, xgboost
### Install XGBoost
On Mac:
```
brew install gcc5
pip install xgboost
```
On Ubuntu (Python package):
```
cd python-package
sudo python setup.py install
```
### Input
The code reads 'data.csv' to train model.
### Output
The test error of using softmax or softprob is printed to the console.
### Usage
Set the parameters according to the result of GridSearchCV.py

## GridSearchCV.py
### Description
Parameter grid search with xgboost
### Requirements
numpy, pandas, scikit-learn, xgboost
### Input
The code reads 'data.csv' to train model.
### Output
The best parameters and the corresponding accuracy of the model is printed to the console.
### Usage
Change the *param_grid* to search the best parameters.
