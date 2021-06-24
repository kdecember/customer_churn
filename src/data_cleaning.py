import os
import sys
module_path = os.path.abspath(os.path.join(os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def create_df(csv):
    relative_filename = os.path.abspath(os.path.join(os.pardir, 'data', csv))
    df1 = pd.read_csv(relative_filename)

    return df1

def fitting(X_train):
    le = LabelEncoder()
    X_train['international plan'] = le.fit(X_train['international plan'])
    X_train['voice mail plan'] = le.fit(X_train['voice mail plan'])
    
    ss = StandardScaler()
    ss.fit(X_train)
    
    return X_train

def transform(X_train, X_test):
    pass