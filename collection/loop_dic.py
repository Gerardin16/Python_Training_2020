# dictionary does not maintaian order
d = {'1': 'one', '2': 'two'}

# get all the items in the key, value tuple
for k,v in d.items():
    print(k, v)

# gets only keys
for k in d.keys():
    print(k)
