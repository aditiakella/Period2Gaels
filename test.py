# code here
import json

# some dictionaries
p1 = { "name":"Sophie", "age":16, "city":"New York"}
p2 = { "name":"Grace", "age":17, "city":"Atlanta"}
p3 = { "name":"Luke", "age":17, "city":"San Diego"}
p4 = { "name": "Aditi", "age": 16, "city": "Whistler"}

# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
print(dict_people)
people = dict_people["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# prepare list for JSON, this can be sent via a browser
json_people = json.dumps(dict_people)
# the result is a JSON file:
print("JSON People")
# write some code to Print People from JSon
print(type(json_people))
people = json.dumps(dict_people["people"])
print(json_people)
x = json.loads(json_people)
people = x["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# unwind people back to JSON
dict_people = json.loads(json_people)
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
x = json.loads(json_people)
people = x["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()