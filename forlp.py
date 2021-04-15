states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI' }
cities = { 'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville' }
for state,abbrev in states.items():
    print("%s is abbreviated %s"%(state,abbrev))
print('_'*50)
for city,expan in cities.items():
    print("%s is abbreviated %s"%(city,expan))
state=states.get('Texas', None)
if not state:
    print("Sorry ,no Texas.")
print('_'*50)
#def breakpoint()
for state,expan in states.items():
    print("%s state is expan %s and has city %s"%(state,expan,cities[expan]))
