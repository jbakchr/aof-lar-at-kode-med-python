"""
EXERCISE

In this exercise you first to create a variable called "car" and assign it a dict with the following key / value pairs:
- 1) "make": "Audi"
- 2) "speed": 280
- 3) "has_wheels": True
- 4) "can_fly": True

After having done so you should now loop through the "car" dict and do the following:
- 1) Whether your car dict has a key called "can_fly" AND if that key is "True
- 2) If the "can_fly" key is set to a value of "True" then change that key to "False"

Lastly just print your car dict to check that it has been updated
"""
car = {"make": "Audi", "speed": 280, "has_wheels": True, "can_fly": True}

for key in car:
  if key == "can_fly" and car[key]:
    car[key] = False

print(car)