# Ejercicio 2

# Planets and moons

from time import monotonic_ns
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# planet_list= ['mercury','venus','earth', 'mars','jupiter','saturn','uranus','neptune','pluto']
moons = planet_moons.values()
print(moons)
planets = len(planet_moons.keys())
print(planets)

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon
# print (total_moons)
# Calcula el promedio
average = (total_moons / planets)
print(average)