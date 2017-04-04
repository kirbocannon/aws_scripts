data = ['cat', 'dog', 'car', 'boat', 'house', 'airplane', 'glasses', 'lotion', 'router', 'switch', 'electric']

print(data[2:5:2])

p = lambda x:x.upper()

for i in data:
    print(p(i))

p = (lambda x: x.upper(), data)
print(p)
