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

## svm_classifier.py
### Description
This file read our preprocessed corpus, selected features, then do the random oversampling to solve the
unbalanced data problem, and use the 10-Fold cross validation to compute the accuracy of the model, and finally use all
the training data to train the final model.
### Requirements
numpy, pandas, imbalanced-learn, scikit-learn, LIBSVM
### Input
The code reads 'data.csv' to train model.
### Output
The average accuracy of svm model by 10-Fold cross validation is printed to the console. The final svm model is saved to 'happiness_index_svm.model'.
### Usage
Let 'data.csv' and 'svm_classifier.py' in the same folder, prepare all the libraries needed, and run.

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
pip install xgboost
```
### Input
The code reads 'data.csv' to train model.
### Output
The test error of using softmax or softprob with hold-out validation or cross-validation is printed to the console.
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
The best parameters and the corresponding accuracy of the model is printed to the console. The best model is printed to the console and is saved in file 'XGB.model'.
### Usage
Change the *param_grid* to search the best parameters.

## predict.py
### Description
Predict happiness index from tweets.
### Requirements
pandas, xgboost
### Input
The code uses the model in 'XGB.model' to do prediction. The code reads all csv file in the folder './test_data/' and do prediction on each dataset.
### Output
The predicted happiness index along with the created time of the tweet are saved in files '*_result.csv' under the folder './predictions/'.
### Usage
Make sure 'XGB.model' is in the same directory, all the test data csv files is in the folder './test_data/' named as 'test_*_nlp.csv', and there is a folder './predictions', then run this python file.

## vis.py
### Description
Visualize twitter users' predicted happiness index using two kinds of graphs: line chart and heat map.
### Requirements
pandas, plotly
### Input
The code reads either a csv file from given filename or all csv files under the given directory ('./predictions/*.csv' by default).
### Output
Two html files are generated as the visualization results of the prediction.
### Usage
Before running, make sure the data files are named as 'test_*_result.csv'.
- Set *aggregate_by_date*: whether the predicted values should be aggregated by date;
- Set *log_value*: whether perform the natural logarithm on the predicted values;
- Select the method of loading data: either load a single csv file or load all csv files under a directory.
