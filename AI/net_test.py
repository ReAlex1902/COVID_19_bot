
## Example of using neural net

from model import *

loaded_model = get_model()

lst = [1, 0, 0, 1, 0, 0, 0, 2]
print(loaded_model(lst))
