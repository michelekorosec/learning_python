import numpy as np

data = np.array([
    ("joe",32,6),
    ("mary",15,20),
    ("felipe",80,100),
    ("beyonce",38,9001),
], dtype=[("name",str,10), ("age",int), ("power",int)])

print(data[0])
print(data["name"])
print(data[data["power"] > 9000]["name"])
print(np.sort(data[data["age"]>20], order="power")["name"])