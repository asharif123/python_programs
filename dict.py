##dict
stuff = {"name": "Zed", "age": 18, "height": 126}
print(stuff["name"])
print(stuff["height"])

##add more info to stuff
stuff["city"] = "Los Angeles"
stuff[1] = "practice"
print(stuff[1])
print(stuff)

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {"CA": "San Francisco", "MI": "Detroit", "Orlando": "FL"}

cities["NY"] = "New York"
cities["OR"] = "Oregon"

print("NY State has", states["New York"])

#print every state abbreviation from states dictionary
for state, abbrev in states.items():
    print("%s is abbreviated %s\n" %(state, abbrev))

#get cities
city = cities.get("CA")
print(city)