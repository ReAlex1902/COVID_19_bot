
import pickle

filename = "Random_Forest.sav"
rf = pickle.load(open(filename, "rb"))

lst = [2, 5, 1, 0, 0, 37, 1, 0]
result = rf.predict_proba([lst])

print(result)
