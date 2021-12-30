import json

person = {
	"name": "Suraj",
	"age": 30,
	"city": "New Delhi"
}
personJson = json.dumps(person, indent=4)

# with open("person.json", "w") as file:
# 	json.dump(person, file, indent=4)

nperson = json.loads(personJson)
print(nperson)
