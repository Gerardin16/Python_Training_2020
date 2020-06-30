counts = dict()
names = ['stalin', 'loyola', 'stalin', 'soosai']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)
 

