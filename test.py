import json

json_test_file = '/Users/KennyB/Downloads/generated.json'
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
data = json.loads(json_string)

print(data['first_name'])



with open(json_test_file) as j:
    jdata = json.load(j)

print(jdata[0]['email'])


hey = ['sup', 'yo']
print(len(hey))

list = ['Hey', 'Sup']

for i in list:
    print(i)

