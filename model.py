import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
import pickle

np.random.seed(1)


# Dictionaries
state = {'ak': 0, 'al': 1, 'ar': 2, 'az': 3, 'ca': 4, 'co': 5, 'ct': 6, 'dc': 7, 'de': 8, 'fl': 9,
         'ga': 10, 'hi': 11, 'ia': 12, 'id': 13, 'il': 14, 'in': 15, 'ks': 16, 'ky': 17, 'la': 18, 'ma': 19,
         'md': 20, 'me': 21, 'mi': 22, 'mn': 23, 'mo': 24, 'ms': 25, 'mt': 26, 'nc': 27, 'nd': 28, 'nh': 29,
         'nj': 30, 'nm': 31, 'nv': 32, 'ny': 33, 'oh': 34, 'ok': 35, 'or': 36, 'pa': 37, 'ri': 38, 'sc': 39,
         'sd': 40, 'tn': 41, 'tx': 42, 'ut': 43, 'va': 44, 'vt': 45, 'wa': 46, 'wi': 47, 'wv': 48, 'wy': 49}
title = {'clean': 0, 'lien': 1, 'rebuilt': 2, 'salvage': 3}
transmission = {'automatic': 0, 'manual': 1, 'other': 2}
drive = {'4wd': 0, 'fwd': 1, 'rwd': 2}


data = pd.read_csv("tacoma_final.csv")

X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


params = {'n_estimators': 500,
          'max_depth': 4,
          'min_samples_split': 5,
          'learning_rate': 0.01,
          'loss': 'ls'}

reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)


pickle.dump(reg, open("model.pkl", "wb"))

model = pickle.load(open("model.pkl", "rb"))
