lst = [1, 2, 3]
# square using square elements
s=[]
for item in lst:
    s.append(item * item)

print(s)


# list comprehension

square = [ item * item for item in lst]
print(square)
