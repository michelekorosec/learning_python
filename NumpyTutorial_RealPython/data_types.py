import numpy as np

a = np.array([1,3,5.5,7.7,9.2], dtype=np.single)

print(a)
print(a.dtype)

b = np.array([1,3,5.5,7.7,9.2], dtype=np.uint8)

print(b)
print(b.dtype)

names = np.array(["bob", "amy", "han"], dtype=str)

print(names)
print(names.dtype)
print(names.itemsize)

names_2 = np.array(["bob", "amy", "han"])

print(names_2)
print(names_2.dtype)
print(names_2.itemsize)

more_names = np.array(["bobo","jehosephat"])
full_names = np.concatenate((names_2,more_names))

print(full_names)
print(full_names.dtype)
print(full_names.itemsize)

emojis = np.array(['⚛','🏎','🐍'])

print(emojis)
print(emojis.dtype)
print(emojis.itemsize)

names_2[2]="jamina"
print(names_2)
