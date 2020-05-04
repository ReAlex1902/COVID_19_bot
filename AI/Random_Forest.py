
## Example of using Ranodom Forest

import pickle

filename = "Random_Forest.sav"
rf = pickle.load(open(filename, "rb"))

lst = [2, 7, 0, 1, 0, 55, 1, 0]
result = rf.predict_proba([lst])

print(result)
