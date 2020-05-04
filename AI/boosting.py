
import pickle
import numpy as np
import pandas as pd

filename = "boosting.sav"
bst = pickle.load(open(filename, "rb"))

lst = [1, 2, 2, 1, 0, 0, 0, 0]
columns = ['cough', 'fever', 'sore_throat', 'shortness_of_breath', 'head_ache',
       'age', 'gender', 'test_indication']
lst = pd.DataFrame(lst, index = columns).T          ## XGB needs dataframe

result = bst.predict_proba(lst)

print(result)
